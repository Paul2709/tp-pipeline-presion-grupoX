# Guía explicativa del trabajo práctico

Este archivo explica la solución de las actividades obligatorias de **Pipeline de control de presión arterial**. Puede utilizarse como preparación para la defensa grupal.

## Parte 0: datos

La fuente original `EstudioPresionEdad.csv` contiene 50 filas con las columnas `Sujeto`, `Edad`, `IMC`, `PresionSistolica` y `Grupo`. La cátedra propone una versión adaptada para el ejercicio: códigos `PAC-001` a `PAC-050`, cabeceras normalizadas y 8 filas intencionalmente defectuosas. Los 50 registros válidos resultan idénticos a los originales. Por lo tanto **el programa principal procesa `mediciones.csv` y no el archivo original sin transformar**. Se incorpora también `mediciones.json` para practicar las dos fuentes.

## Parte 1: fuentes de datos

La clase abstracta `FuenteDatos` declara `cargar(ruta)`. `FuenteCSV` lee el formato CSV con `csv.DictReader`, que produce diccionarios cuyos valores son cadenas. `FuenteJSON` utiliza `json.load`, que respeta números y valores `null` (`None` en Python). Su objetivo es ofrecer el mismo tipo de salida (lista de diccionarios) independientemente del formato. Si no existe el archivo, la excepción `FileNotFoundError` se propaga al programa, sin ocultarse.

## Parte 2: el modelo Paciente

Cada instancia representa un registro que **ya fue validado**. El constructor guarda los cinco atributos. `franja_etaria()` devuelve `18-39`, `40-59` o `60+`; `es_hipertenso()` compara la presión sistólica con el umbral didáctico 140. El método `__str__()` devuelve una presentación que permite imprimir al paciente de forma legible.

## Parte 3: validar y limpiar

`PATRON_CODIGO` se compiló con `re.compile(r"PAC-\d{3}")`. `fullmatch` comprueba toda la cadena, a diferencia de `search`, que podría encontrar un patrón dentro de otra cadena. `convertir_numero` transforma números escritos como texto a `float`; los valores vacíos o `None` se convierten en `None`. Un texto como `abc` produce `ValueError`.

`validar_registro` comprueba que el código tenga el formato requerido, que edad (18–100), IMC (12–60) y presión sistólica (70–250) estén presentes y en rango, y que el grupo sea A o B. Devuelve una lista de motivos. Deja el chequeo de duplicados para `limpiar`, porque solo al recorrer la lista completa puede conocerse si un código ya apareció.

`limpiar` recorre cada fila, empieza a numerarlas desde 1 y conserva solo la primera entrada **válida** por código. Cuando se rechaza una fila, registra `fila`, `codigo` y `motivo`. Para los válidos construye instancias de `Paciente`. No modifica los registros recibidos.

## Parte 4: reporte y exportación

`generar_reporte` recorre los grupos en orden A y B, cuenta los pacientes válidos en cada grupo y calcula la presión sistólica media (`suma / cantidad`) y la proporción de hipertensos (`casos / cantidad`). Redondea a dos y tres decimales, respectivamente, y devuelve 0 cuando el grupo no tiene pacientes, evitando divisiones por cero.

`guardar_csv` usa `csv.DictWriter`: toma las claves del primer diccionario como nombres de columnas, escribe el encabezado y luego las filas. Los resultados se guardan en `outputs/reporte.csv` y `outputs/rechazos.csv`.

## Parte 5: pruebas automáticas

Los tests provistos por la cátedra examinan tanto CSV como JSON, comprueban que hay 50 válidos y 8 rechazados, detectan archivos inexistentes y estructuras JSON inválidas, verifican los límites de las franjas etarias y el umbral de 140 mmHg, comparan ambos reportes, revisan que el duplicado conserve la primera aparición y comparan valores de control estadísticos (incluida la correlación edad-presión, cercana a 0,794). Resultado comprobado: `Todas las pruebas pasaron.`

## Parte 6: repositorio

Desde la raíz del proyecto:

```bash
python src/main.py data/mediciones.csv
python tests/test_pipeline.py
```

Una vez que el grupo haya completado su nombre y composición en README.md, crear un repositorio público en GitHub con los archivos del proyecto. Dividir los avances en un mínimo de tres commits con cambios reales; por ejemplo:

```bash
git init
git add data/ src/fuentes.py src/modelo.py .gitignore
git commit -m "Agrega datos y fuentes CSV y JSON"
git add src/pipeline.py
git commit -m "Implementa validacion limpieza y reporte"
git add src/main.py tests/ README.md GUIA_EXPLICATIVA.md TP_Grupal_Pipeline_Presion_RESUELTO.ipynb
git commit -m "Agrega programa principal pruebas y documentacion"
```

Configurar el repositorio remoto y usar `git push` para publicar. No se generaron commits en este archivo ZIP, de modo que los commits deben hacerse realmente durante el trabajo del grupo.

## Resultados comprobados

- Registros de entrada: 58.
- Registros válidos: 50.
- Rechazos: 8 (filas 6, 17, 23, 34, 40, 46, 52 y 58).
- Grupo A: 27 pacientes, presión media 127,26 mmHg y proporción de hipertensión 0,185.
- Grupo B: 23 pacientes, presión media 118,61 mmHg y proporción de hipertensión 0,130.
- Se conservan los registros válidos originales y se rechazan solamente las 8 entradas defectuosas.

## Limitaciones

Las mediciones son simuladas. La correlación estadística no indica necesariamente causalidad. Un registro con presión de 140 mmHg o más se considera hipertenso **solo a efectos didácticos**, no como diagnóstico clínico. Se asume un solo registro aceptado por código y no se realizan imputaciones de datos faltantes.
