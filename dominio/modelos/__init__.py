"""Modelos del dominio académico."""

from dominio.modelos.alumno import Alumno, AlumnoBecado, AlumnoRegular
from dominio.modelos.colegio import Colegio, ColegioPrivado, ColegioPublico

__all__ = [
    "Alumno",
    "AlumnoBecado",
    "AlumnoRegular",
    "Colegio",
    "ColegioPrivado",
    "ColegioPublico",
]

