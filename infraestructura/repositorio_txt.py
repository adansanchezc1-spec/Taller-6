"""Repositorio TXT para persistencia del sistema escolar."""

from __future__ import annotations

from pathlib import Path

from aplicacion.repositorio_institucional import RepositorioInstitucional
from dominio.fabricas import FabricaAlumnos, FabricaColegios
from dominio.modelos.alumno import Alumno
from dominio.modelos.colegio import Colegio


class RepositorioTXT(RepositorioInstitucional):
    """Implementación de persistencia en archivo plano."""

    seccion_colegios = "[COLEGIOS]"
    seccion_alumnos = "[ALUMNOS]"

    def __init__(self, ruta_archivo: Path) -> None:
        self._ruta_archivo = ruta_archivo

    def existe_fuente(self) -> bool:
        return self._ruta_archivo.exists()

    def guardar_colegios(self, colegios: list[Colegio]) -> None:
        self._ruta_archivo.parent.mkdir(parents=True, exist_ok=True)
        lineas = [self.seccion_colegios]
        lineas.extend(colegio.serializar() for colegio in colegios)
        lineas.append("")
        lineas.append(self.seccion_alumnos)
        for colegio in colegios:
            lineas.extend(alumno.serializar() for alumno in colegio.alumnos)
        contenido = "\n".join(lineas) + "\n"
        self._ruta_archivo.write_text(contenido, encoding="utf-8")

    def cargar_colegios(self) -> list[Colegio]:
        if not self.existe_fuente():
            return []

        colegios_por_id: dict[str, Colegio] = {}
        alumnos_pendientes: list[Alumno] = []
        seccion_actual = ""

        for linea in self._ruta_archivo.read_text(encoding="utf-8").splitlines():
            contenido = linea.strip()
            if not contenido:
                continue
            if contenido == self.seccion_colegios:
                seccion_actual = "colegios"
                continue
            if contenido == self.seccion_alumnos:
                seccion_actual = "alumnos"
                continue

            if seccion_actual == "colegios":
                colegio = self._deserializar_colegio(contenido)
                colegios_por_id[colegio.identificador] = colegio
                continue

            if seccion_actual == "alumnos":
                alumnos_pendientes.append(self._deserializar_alumno(contenido))

        for alumno in alumnos_pendientes:
            if not alumno.colegio_id or alumno.colegio_id not in colegios_por_id:
                raise ValueError(
                    "El archivo TXT contiene un alumno asociado a un colegio inexistente."
                )
            colegios_por_id[alumno.colegio_id].agregar_alumno(alumno)

        return list(colegios_por_id.values())

    @staticmethod
    def _deserializar_colegio(registro: str) -> Colegio:
        partes = registro.split("|", maxsplit=2)
        if len(partes) != 3:
            raise ValueError("Registro de colegio inválido en el archivo TXT.")
        tipo, identificador, nombre = partes
        return FabricaColegios.crear(tipo, identificador, nombre)

    @staticmethod
    def _deserializar_alumno(registro: str) -> Alumno:
        partes = registro.split("|", maxsplit=5)
        if len(partes) != 6:
            raise ValueError("Registro de alumno inválido en el archivo TXT.")
        perfil, identificador, colegio_id, nombre, edad, grado = partes
        return FabricaAlumnos.crear(
            perfil=perfil,
            identificador=identificador,
            nombre=nombre,
            edad=int(edad),
            grado=grado,
            colegio_id=colegio_id,
        )

