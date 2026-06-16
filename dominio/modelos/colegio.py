"""Modelos de colegio para el dominio institucional."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from dominio.modelos.alumno import Alumno


@dataclass(slots=True)
class Colegio(ABC):
    """Representa el comportamiento común de un colegio."""

    _identificador: str
    _nombre: str
    alumnos: list[Alumno] = field(default_factory=list)

    def __post_init__(self) -> None:
        self._validar_cadenas(self._identificador, "El identificador del colegio")
        self._validar_cadenas(self._nombre, "El nombre del colegio")

    @staticmethod
    def _validar_cadenas(valor: str, campo: str) -> None:
        if not valor or not valor.strip():
            raise ValueError(f"{campo} es obligatorio.")
        if "|" in valor:
            raise ValueError(f"{campo} no puede contener el carácter '|'.")

    @abstractmethod
    def tipo(self) -> str:
        """Retorna el tipo concreto del colegio."""

    @abstractmethod
    def costo_base_matricula(self) -> int:
        """Retorna el costo base de matrícula del colegio."""

    def agregar_alumno(self, alumno: Alumno) -> None:
        """Asocia un alumno con el colegio."""
        alumno.colegio_id = self._identificador
        self.alumnos.append(alumno)

    def calcular_matricula(self, alumno: Alumno) -> int:
        """Calcula la matrícula final de un alumno asociado al colegio."""
        return alumno.calcular_valor_matricula(self.costo_base_matricula())

    def serializar(self) -> str:
        """Convierte el colegio a una línea del archivo TXT."""
        return f"{self.tipo().upper()}|{self._identificador}|{self._nombre}"

    def resumen(self) -> str:
        """Retorna un resumen legible del colegio."""
        return (
            f"{self._identificador} - {self._nombre} | "
            f"Tipo: {self.tipo()} | Alumnos: {len(self.alumnos)}"
        )

    @property
    def identificador(self) -> str:
        """Acceso de lectura al identificador del colegio."""
        return self._identificador

    @property
    def nombre(self) -> str:
        """Acceso de lectura al nombre del colegio."""
        return self._nombre


@dataclass(slots=True)
class ColegioPublico(Colegio):
    """Colegio con costo base subsidiado."""

    def tipo(self) -> str:
        return "PUBLICO"

    def costo_base_matricula(self) -> int:
        return 50000


@dataclass(slots=True)
class ColegioPrivado(Colegio):
    """Colegio con costo base privado."""

    def tipo(self) -> str:
        return "PRIVADO"

    def costo_base_matricula(self) -> int:
        return 150000

