"""Servicios de aplicación para la gestión escolar."""

from __future__ import annotations

from aplicacion.repositorio_institucional import RepositorioInstitucional
from dominio.fabricas import FabricaAlumnos, FabricaColegios
from dominio.modelos.alumno import Alumno
from dominio.modelos.colegio import Colegio


class ServicioGestionEscolar:
    """Coordina los casos de uso del sistema escolar."""

    def __init__(self, repositorio: RepositorioInstitucional) -> None:
        self._repositorio = repositorio
        self._colegios: list[Colegio] = []

    def existe_archivo_guardado(self) -> bool:
        """Indica si existe información persistida."""
        return self._repositorio.existe_fuente()

    def cargar_si_existe(self) -> bool:
        """Carga la información solo si el archivo existe."""
        if not self.existe_archivo_guardado():
            return False
        self.cargar_datos()
        return True

    def cargar_datos(self) -> list[Colegio]:
        """Reemplaza el estado en memoria con lo persistido."""
        self._colegios = self._repositorio.cargar_colegios()
        return self.listar_colegios()

    def guardar_datos(self) -> None:
        """Persiste el estado actual del sistema."""
        self._repositorio.guardar_colegios(self._colegios)

    def registrar_colegio(self, nombre: str, tipo: str) -> Colegio:
        """Registra un colegio nuevo."""
        identificador = self._siguiente_identificador(
            prefijo="COL",
            identificadores=[colegio.identificador for colegio in self._colegios],
        )
        colegio = FabricaColegios.crear(tipo, identificador, nombre)
        self._colegios.append(colegio)
        return colegio

    def registrar_alumno(
        self,
        colegio_id: str,
        nombre: str,
        edad: int,
        grado: str,
        perfil: str,
    ) -> Alumno:
        """Registra un alumno en un colegio existente."""
        colegio = self.obtener_colegio(colegio_id)
        identificador = self._siguiente_identificador(
            prefijo="ALU",
            identificadores=[
                alumno.identificador
                for colegio_actual in self._colegios
                for alumno in colegio_actual.alumnos
            ],
        )
        alumno = FabricaAlumnos.crear(
            perfil=perfil,
            identificador=identificador,
            nombre=nombre,
            edad=edad,
            grado=grado,
            colegio_id=colegio.identificador,
        )
        colegio.agregar_alumno(alumno)
        return alumno

    def listar_colegios(self) -> list[Colegio]:
        """Retorna una copia de los colegios registrados."""
        return list(self._colegios)

    def obtener_colegio(self, colegio_id: str) -> Colegio:
        """Busca un colegio por su identificador."""
        for colegio in self._colegios:
            if colegio.identificador == colegio_id:
                return colegio
        raise ValueError(f"No existe un colegio con el identificador {colegio_id}.")

    def listar_alumnos_por_colegio(self, colegio_id: str) -> list[Alumno]:
        """Retorna los alumnos asociados a un colegio."""
        colegio = self.obtener_colegio(colegio_id)
        return list(colegio.alumnos)

    def obtener_resumen_matriculas(self) -> list[dict[str, str | int]]:
        """Genera un resumen polimórfico de matrículas."""
        resumen: list[dict[str, str | int]] = []
        for colegio in self._colegios:
            for alumno in colegio.alumnos:
                resumen.append(
                    {
                        "colegio_id": colegio.identificador,
                        "colegio_nombre": colegio.nombre,
                        "colegio_tipo": colegio.tipo(),
                        "alumno_id": alumno.identificador,
                        "alumno_nombre": alumno.nombre,
                        "perfil": alumno.perfil(),
                        "grado": alumno.grado,
                        "valor_base": colegio.costo_base_matricula(),
                        "valor_final": colegio.calcular_matricula(alumno),
                    }
                )
        return resumen

    @staticmethod
    def _siguiente_identificador(
        prefijo: str, identificadores: list[str]
    ) -> str:
        mayor_actual = 0
        for identificador in identificadores:
            partes = identificador.split("-")
            if len(partes) != 2 or partes[0] != prefijo:
                continue
            try:
                mayor_actual = max(mayor_actual, int(partes[1]))
            except ValueError:
                continue
        return f"{prefijo}-{mayor_actual + 1:03d}"

