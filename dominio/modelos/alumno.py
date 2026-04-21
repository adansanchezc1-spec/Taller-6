"""Modelos de alumno para el dominio institucional."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(slots=True)
class Alumno(ABC):
    """Representa el comportamiento común de un alumno."""

    identificador: str
    nombre: str
    edad: int
    grado: str
    colegio_id: str | None = None

    def __post_init__(self) -> None:
        self._validar_cadenas(self.identificador, "El identificador del alumno")
        self._validar_cadenas(self.nombre, "El nombre del alumno")
        self._validar_cadenas(self.grado, "El grado del alumno")
        if self.edad <= 0:
            raise ValueError("La edad del alumno debe ser un número positivo.")

    @staticmethod
    def _validar_cadenas(valor: str, campo: str) -> None:
        if not valor or not valor.strip():
            raise ValueError(f"{campo} es obligatorio.")
        if "|" in valor:
            raise ValueError(f"{campo} no puede contener el carácter '|'.")

    @abstractmethod
    def perfil(self) -> str:
        """Retorna el perfil académico del alumno."""

    @abstractmethod
    def porcentaje_descuento(self) -> float:
        """Retorna el porcentaje de descuento aplicado a la matrícula."""

    def calcular_valor_matricula(self, valor_base: int) -> int:
        """Calcula el valor final de la matrícula."""
        descuento = int(valor_base * self.porcentaje_descuento())
        return valor_base - descuento

    def serializar(self) -> str:
        """Convierte el alumno a una línea del archivo TXT."""
        colegio_id = self.colegio_id or ""
        return (
            f"{self.perfil().upper()}|{self.identificador}|{colegio_id}|"
            f"{self.nombre}|{self.edad}|{self.grado}"
        )

    def descripcion(self, valor_base: int) -> str:
        """Retorna un resumen legible del alumno y su matrícula."""
        valor_final = self.calcular_valor_matricula(valor_base)
        descuento = int(self.porcentaje_descuento() * 100)
        return (
            f"{self.identificador} - {self.nombre} | Grado: {self.grado} | "
            f"Perfil: {self.perfil()} | Descuento: {descuento}% | "
            f"Matrícula final: ${valor_final}"
        )


@dataclass(slots=True)
class AlumnoRegular(Alumno):
    """Alumno sin beneficios de descuento."""

    def perfil(self) -> str:
        return "REGULAR"

    def porcentaje_descuento(self) -> float:
        return 0.0


@dataclass(slots=True)
class AlumnoBecado(Alumno):
    """Alumno que recibe una beca institucional."""

    def perfil(self) -> str:
        return "BECADO"

    def porcentaje_descuento(self) -> float:
        return 0.5

