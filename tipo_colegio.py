"""Alias de compatibilidad para tipos de colegio."""

from dominio.modelos.colegio import ColegioPrivado, ColegioPublico

col_privado = ColegioPrivado
col_publico = ColegioPublico

__all__ = ["ColegioPrivado", "ColegioPublico", "col_privado", "col_publico"]
