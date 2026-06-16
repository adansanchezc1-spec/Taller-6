"""Factorías del dominio para crear subtipos concretos."""

from __future__ import annotations

from dominio.modelos.alumno import Alumno, AlumnoBecado, AlumnoRegular
from dominio.modelos.colegio import Colegio, ColegioPrivado, ColegioPublico


class FabricaColegios:
    """Factory Method para construir colegios concretos."""

    _tipos: dict[str, type[Colegio]] = {
        "PUBLICO": ColegioPublico,
        "PRIVADO": ColegioPrivado,
    }

    @classmethod
    def crear(cls, tipo: str, identificador: str, nombre: str) -> Colegio:
        tipo_normalizado = tipo.strip().upper()
        clase = cls._tipos.get(tipo_normalizado)
        if clase is None:
            raise ValueError(f"Tipo de colegio no soportado: {tipo}.")
        return clase(_identificador=identificador, _nombre=nombre)


class FabricaAlumnos:
    """Factory Method para construir alumnos concretos."""

    _tipos: dict[str, type[Alumno]] = {
        "REGULAR": AlumnoRegular,
        "BECADO": AlumnoBecado,
    }

    @classmethod
    def crear(
        cls,
        perfil: str,
        identificador: str,
        nombre: str,
        edad: int,
        grado: str,
        colegio_id: str | None = None,
    ) -> Alumno:
        perfil_normalizado = perfil.strip().upper()
        clase = cls._tipos.get(perfil_normalizado)
        if clase is None:
            raise ValueError(f"Perfil de alumno no soportado: {perfil}.")
        return clase(
            _identificador=identificador,
            _nombre=nombre,
            _edad=edad,
            _grado=grado,
            _colegio_id=colegio_id,
        )

