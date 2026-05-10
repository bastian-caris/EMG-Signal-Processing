# Subconjunto de Datos de Electromiografía (EMG) en Marcha Normal

## 1. Fuente y Citación
Este conjunto de datos es un subconjunto derivado de la investigación "EMG dataset in Lower Limb".
* **Autores:** Sanchez, O. & Sotelo, J. (2014).
* **Repositorio:** UCI Machine Learning Repository.
* **DOI / Enlace:** [https://doi.org/10.24432/C5ZW3P]

## 2. Alcance del Conjunto de Datos
Esta colección específica incluye únicamente los datos del **Grupo N (Normal/Control)**. Se han excluido los sujetos con patologías de rodilla (Grupo A) y se han omitido las pruebas estáticas (sentado/de pie).

* **Cantidad de Sujetos:** 11 individuos sanos.
* **Actividad:** Marcha (caminata a ritmo seleccionado por el sujeto).
* **Objetivo:** Establecer una línea de base de la actividad muscular y la cinemática de la rodilla en un ciclo de marcha estándar y saludable.

## 3. Especificaciones Técnicas
* **Frecuencia de Muestreo:** 1000 Hz.
* **Resolución:** 14 bits.
* **Unidades:** * Los canales de EMG (RF, BF, VM, ST) están expresados en **Milivoltios (mV)**.
    * El canal cinemático (FX) está expresado en **Grados (°)**.

## 4. Definición de Columnas
Los archivos están organizados de la siguiente forma:

| Columna | Descripción | Tipo de Dato |
| :--- | :--- | :--- |
| **Time_s** | Marca de tiempo calculada en segundos | Temporal |
| **RF** | Actividad del músculo Rectus Femoris | EMG |
| **BF** | Actividad del músculo Biceps Femoris | EMG |
| **VM** | Actividad del músculo Vastus Medialis | EMG |
| **ST** | Actividad del músculo Semitendinosus | EMG |
| **FX** | Ángulo de Flexión de la Rodilla | Cinemático |
