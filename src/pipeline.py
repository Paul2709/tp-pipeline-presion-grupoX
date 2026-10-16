"""Validación, limpieza y reportes de presión sistólica."""

import csv
import re

from modelo import Paciente


PATRON_CODIGO = re.compile(r"PAC-\d{3}")
RANGOS = {
    "edad": (18, 100),
    "imc": (12, 60),
    "presion_sistolica": (70, 250),
}
GRUPOS_VALIDOS = ("A", "B")


def convertir_numero(valor):
    """Devuelve None si falta un dato y float si es un número."""
    if valor is None:
        return None
    if isinstance(valor, str) and not valor.strip():
        return None
    return float(valor)


def validar_registro(registro):
    """Devuelve una lista de motivos, vacía para registros válidos."""
    motivos = []
    codigo = registro.get("codigo")

    if not isinstance(codigo, str) or not PATRON_CODIGO.fullmatch(codigo):
        motivos.append("código con formato inválido")

    for campo, (minimo, maximo) in RANGOS.items():
        try:
            numero = convertir_numero(registro.get(campo))
        except (ValueError, TypeError):
            motivos.append(f"{campo} no numérico")
            continue

        if numero is None:
            motivos.append(f"{campo} faltante")
        elif not minimo <= numero <= maximo:
            motivos.append(f"{campo} fuera de rango")

    if registro.get("grupo") not in GRUPOS_VALIDOS:
        motivos.append("grupo inválido")

    return motivos


def limpiar(registros):
    """Separa pacientes válidos y rechazos con fila, código y motivo."""
    validos = []
    rechazos = []
    codigos_aceptados = set()

    for numero_fila, registro in enumerate(registros, start=1):
        motivos = validar_registro(registro)
        codigo = registro.get("codigo")

        if codigo in codigos_aceptados:
            motivos.append("código duplicado")

        if motivos:
            rechazos.append({
                "fila": numero_fila,
                "codigo": codigo,
                "motivo": "; ".join(motivos),
            })
            continue

        paciente = Paciente(
            codigo=codigo,
            edad=convertir_numero(registro["edad"]),
            imc=convertir_numero(registro["imc"]),
            presion=convertir_numero(registro["presion_sistolica"]),
            grupo=registro["grupo"],
        )
        validos.append(paciente)
        codigos_aceptados.add(codigo)

    return validos, rechazos


def generar_reporte(pacientes):
    """Devuelve un resumen de cantidad, promedio y proporción por grupo."""
    reporte = []

    for grupo in GRUPOS_VALIDOS:
        pacientes_grupo = [p for p in pacientes if p.grupo == grupo]
        cantidad = len(pacientes_grupo)

        if cantidad:
            presion_media = round(
                sum(p.presion for p in pacientes_grupo) / cantidad, 2
            )
            proporcion = round(
                sum(p.es_hipertenso() for p in pacientes_grupo) / cantidad,
                3,
            )
        else:
            presion_media = 0.0
            proporcion = 0.0

        reporte.append({
            "grupo": grupo,
            "cantidad": cantidad,
            "presion_media": presion_media,
            "proporcion_hipertensos": proporcion,
        })

    return reporte


def guardar_csv(filas, ruta):
    """Guarda una lista no vacía de diccionarios en un CSV."""
    with open(ruta, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=filas[0].keys())
        escritor.writeheader()
        escritor.writerows(filas)
