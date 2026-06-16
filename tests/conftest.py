"""Configuracion compartida para la suite de pruebas."""

from __future__ import annotations

import shutil
import sys
import uuid
from pathlib import Path
from collections.abc import Iterator

import pytest

sys.dont_write_bytecode = True


@pytest.fixture
def tmp_path() -> Iterator[Path]:
    """Crea directorios temporales dentro del proyecto para evitar permisos externos."""
    base_temporal = Path(__file__).resolve().parent.parent / ".pytest_tmp"
    base_temporal.mkdir(exist_ok=True)
    ruta = base_temporal / f"pytest-{uuid.uuid4().hex}"
    ruta.mkdir()
    try:
        yield ruta
    finally:
        shutil.rmtree(ruta, ignore_errors=True)
