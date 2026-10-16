"""Lectura de archivos de mediciones en formatos CSV y JSON."""

import csv
import json
from abc import ABC, abstractmethod


class FuenteDatos(ABC):
    """Interfaz que comparten todas las fuentes de datos."""

    @abstractmethod
    def cargar(self, ruta):
        """Lee registros y devuelve una lista de diccionarios."""
        pass


class FuenteCSV(FuenteDatos):
    """Fuente de datos que lee archivos CSV."""

    def cargar(self, ruta):
        with open(ruta, encoding="utf-8", newline="") as archivo:
            return list(csv.DictReader(archivo))


class FuenteJSON(FuenteDatos):
    """Fuente de datos que lee archivos JSON."""

    def cargar(self, ruta):
        with open(ruta, encoding="utf-8") as archivo:
            registros = json.load(archivo)

        if not isinstance(registros, list):
            raise ValueError("El archivo JSON debe contener una lista")

        return registros
