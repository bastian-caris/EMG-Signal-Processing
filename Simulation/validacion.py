import os
import time
import mujoco
import mujoco.viewer
import numpy as np

# 1. Cargar el modelo bipedal
directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_xml = os.path.join(directorio_actual, "protesis_base.xml")

with open(ruta_xml, 'r', encoding='utf-8') as archivo:
    model = mujoco.MjModel.from_xml_string(archivo.read())
data = mujoco.MjData(model)

# --- GANANCIAS PD PARA 4 ARTICULACIONES ---
# Orden: [Cadera Der, Rodilla Der, Cadera Izq, Rodilla Izq]
Kp = np.array([40.0, 25.0, 40.0, 25.0])  
Kd = np.array([3.0,  1.5,  3.0,  1.5])    

frecuencia = 0.5
omega = 2 * np.pi * frecuencia

# Índices exactos de las articulaciones con motor en el vector qpos y qvel
idx_activos = [0, 1, 3, 4]

with mujoco.viewer.launch_passive(model, data) as viewer:
    start_time = time.time()
    print("--- Simulación Bípeda: Marcha alternada con desfase de 180° ---")
    
    while viewer.is_running():
        step_start = time.time()
        t = time.time() - start_time
        
        # ================== PIERNA DERECHA (Fase base: w*t) ==================
        fase_der = omega * t
        seno_der = np.sin(fase_der)
        
        q_cadera_der = 0.35 * seno_der
        v_cadera_der = 0.35 * omega * np.cos(fase_der)
        
        if seno_der > 0: # Fase de Balanceo Derecha
            q_rodilla_der = 1.15 * seno_der
            v_rodilla_der = 1.15 * omega * np.cos(fase_der)
        else:            # Fase de Apoyo Derecha
            q_rodilla_der = 0.05
            v_rodilla_der = 0.0

        # ================== PIERNA IZQUIERDA (Desfase de +pi radianes) ==================
        fase_izq = omega * t + np.pi
        seno_izq = np.sin(fase_izq)
        
        q_cadera_izq = 0.35 * seno_izq
        v_cadera_izq = 0.35 * omega * np.cos(fase_izq)
        
        if seno_izq > 0: # Fase de Balanceo Izquierda
            q_rodilla_izq = 1.15 * seno_izq
            v_rodilla_izq = 1.15 * omega * np.cos(fase_izq)
        else:            # Fase de Apoyo Izquierda
            q_rodilla_izq = 0.05
            v_rodilla_izq = 0.0

        # 2. VECTORIZACIÓN DE REFERENCIAS [4 actuadores]
        q_ref = np.array([q_cadera_der, q_rodilla_der, q_cadera_izq, q_rodilla_izq])
        v_ref = np.array([v_cadera_der, v_rodilla_der, v_cadera_izq, v_rodilla_izq])
        
        # 3. LECTURA DE SENSORES FILTRANDO ARTICULACIONES PASIVAS
        q_actual = data.qpos[idx_activos]
        v_actual = data.qvel[idx_activos]
        
        # 4. LEY DE CONTROL PD
        torques = Kp * (q_ref - q_actual) + Kd * (v_ref - v_actual)
        
        # Enviar comandos de torque a los 4 motores
        data.ctrl[:] = torques
        
        # Monitoreo en terminal
        if int(t * 10) % 5 == 0:
            print(f"Torques (Nm) -> Cad.Der: {torques[0]:5.1f} | Rod.Der: {torques[1]:5.1f} || Cad.Izq: {torques[2]:5.1f} | Rod.Izq: {torques[3]:5.1f}")
        
        mujoco.mj_step(model, data)
        viewer.sync()
        
        time_until_next_step = model.opt.timestep - (time.time() - step_start)
        if time_until_next_step > 0:
            time.sleep(time_until_next_step)