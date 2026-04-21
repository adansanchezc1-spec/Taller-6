"""Abstracción del repositorio institucional."""

from __future__ import annotations

from abc import ABC, abstractmethod

from dominio.modelos.colegio import Colegio


class RepositorioInstitucional(ABC):
    """Define el contrato de persistencia del sistema."""

    @abstractmethod
    def existe_fuente(self) -> bool:
        """Indica si existe una fuente de datos persistida."""

    @abstractmethod
    def guardar_colegios(self, colegios: list[Colegio]) -> None:
        """Persiste la lista completa de colegios y alumnos."""

    @abstractmethod
    def cargar_colegios(self) -> list[Colegio]:
        """Recupera los colegios y alumnos persistidos."""

