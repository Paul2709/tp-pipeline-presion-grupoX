# Datos del estudio

- **Origen:** `EstudioPresionEdad.csv`, datos simulados con fines didácticos, provistos por la cátedra para un TP de correlación y regresión.
- **Observaciones originales:** 50.
- **Versión adaptada:** 50 registros originales y 8 registros agregados que contienen errores de carga; CSV y JSON tienen 58 entradas equivalentes.
- **Unidad de análisis:** un paciente adulto con una medición.
- **Variables:** `codigo` (identificador), `edad` (años), `imc` (kg/m²), `presion_sistolica` (mmHg) y `grupo` (A: control, B: intervención).
- **Valores válidos:** edad 18–100, IMC 12–60, presión sistólica 70–250, grupo A o B, código `PAC-` seguido de tres dígitos.
- **Limitaciones:** datos simulados y umbral simplificado de 140 mmHg, que no equivale a una evaluación médica.
