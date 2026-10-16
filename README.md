# Trabajo Práctico Grupal — Pipeline de Control de Presión Arterial

## 1. Integrantes del grupo

- Integrante 1: Paul Chavez Neira

**Materia:** Programación Orientada a Datos  
**Carrera:** Licenciatura en Ciencia de Datos

## 2. Descripción del proyecto

Este trabajo práctico consiste en desarrollar un pipeline de procesamiento de datos utilizando Python.

El programa permite leer información de pacientes desde archivos CSV y JSON, validar los registros, identificar errores, limpiar los datos y generar reportes estadísticos sobre la presión arterial.

## 3. Objetivos

- Implementar clases y herencia mediante programación orientada a objetos.
- Leer archivos CSV y JSON.
- Validar datos utilizando expresiones regulares.
- Detectar registros incorrectos y duplicados.
- Crear objetos de la clase Paciente.
- Calcular estadísticas descriptivas.
- Exportar reportes en formato CSV.
- Verificar el funcionamiento mediante pruebas automáticas.

## 4. Estructura del proyecto

- **data/**: archivos originales y adaptados del estudio.
- **src/**: código fuente del programa.
  - `fuentes.py`: lectura de CSV y JSON.
  - `modelo.py`: clase Paciente.
  - `pipeline.py`: validación, limpieza y reportes.
  - `main.py`: ejecución del pipeline.
- **tests/**: pruebas automáticas del programa.
- **GUIA_EXPLICATIVA.md**: explicación del funcionamiento.
- **README.md**: documentación principal.

## 5. Datos utilizados

Se utiliza el archivo `EstudioPresionEdad.csv`, que contiene 50 registros originales de pacientes.

La versión adaptada del estudio incorpora 8 registros con errores para poner a prueba los procesos de validación y limpieza.

El conjunto de prueba contiene 58 registros en total.

## 6. Ejecución del programa

Se requiere Python 3.

Desde la carpeta principal del proyecto, ejecutar el siguiente comando:

`python src/main.py data/mediciones.csv`

El programa procesa los registros y genera:

- `outputs/reporte.csv`: reporte estadístico por grupo.
- `outputs/rechazos.csv`: registros rechazados y motivos.

## 7. Pruebas automáticas

Para ejecutar las pruebas:

`python tests/test_pipeline.py`

Las pruebas permiten comprobar la lectura de archivos, las validaciones, la eliminación de duplicados y los reportes estadísticos.

## 8. Resultados esperados

| Indicador | Resultado |
|---|---:|
| Registros originales | 50 |
| Registros procesados | 58 |
| Registros válidos | 50 |
| Registros rechazados | 8 |
| Pacientes del grupo A | 27 |
| Pacientes del grupo B | 23 |
| Presión media del grupo A | 127,26 mmHg |
| Presión media del grupo B | 118,61 mmHg |

## 9. Herramientas utilizadas

- Python 3
- Bibliotecas estándar de Python
- Google Colab
- Git y GitHub

## 10. Conclusión

El proyecto permite aplicar conceptos de programación orientada a objetos, manipulación de archivos, validación y limpieza de datos, modularización y pruebas automáticas.

El pipeline transforma datos de entrada en información organizada y permite obtener resultados estadísticos reproducibles.

Los datos utilizados son simulados y tienen fines exclusivamente educativos.
