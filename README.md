# EMG Signal Processing

> Biomedical EMG signal processing project using Python and Jupyter Notebook.

## Description / Descripción

**EN:** Preliminary analysis of surface EMG signals from 11 subjects, including temporal visualization, basic metrics, temporal discretization, quantization error, artifact inspection and frequency analysis via FFT.

**ES:** Análisis preliminar de señales EMG superficiales de 11 sujetos, incluyendo visualización temporal, métricas básicas, discretización temporal, error de cuantización, inspección de artefactos y análisis frecuencial mediante FFT.

## Project Structure / Estructura del proyecto

---

## Configuration / Configuración

**EN:** The analysis runs on one subject and one EMG channel at a time. To change them, modify these two variables at the top of the script:

**ES:** El análisis corre sobre un sujeto y un canal EMG a la vez. Para cambiarlos, modificar estas dos variables al inicio del script:

```python
SUJETO = "1Nmar"   # Opciones: "1Nmar", "2Nmar", ..., "11Nmar"
CANAL  = "RF"      # Opciones: "RF", "BF", "VM", "ST"
```

### Subjects / Sujetos
**EN:** The dataset contains 11 subjects: `1Nmar` to `11Nmar`. By default, subject `1Nmar` is used for demonstration purposes.

**ES:** El dataset contiene 11 sujetos: `1Nmar` hasta `11Nmar`. Por defecto se utiliza el sujeto `1Nmar` como muestra representativa del análisis.

### EMG Channels / Canales EMG
| Canal | Músculo | Muscle |
|-------|---------|--------|
| RF | Rectus Femoris | Rectus Femoris |
| BF | Bíceps Femoral | Biceps Femoris |
| VM | Vasto Medial | Vastus Medialis |
| ST | Semitendinoso | Semitendinosus |

**EN:** By default the analysis uses the `RF` (Rectus Femoris) channel, as it is one of the most representative muscles in gait biomechanics.

**ES:** Por defecto se analiza el canal `RF` (Rectus Femoris), por ser uno de los músculos más representativos en biomecánica de la marcha.

---

## Requirements / Requisitos

```bash
pip install numpy pandas matplotlib scipy
```

---

