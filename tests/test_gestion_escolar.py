"""Pruebas unitarias para el Taller 6."""

from __future__ import annotations

from pathlib import Path
import sys

RAIZ_PROYECTO = Path(__file__).resolve().parents[1]
if str(RAIZ_PROYECTO) not in sys.path:
    sys.path.insert(0, str(RAIZ_PROYECTO))

import pytest

from aplicacion.servicio_gestion_escolar import ServicioGestionEscolar
from dominio.fabricas import FabricaAlumnos, FabricaColegios
from infraestructura.repositorio_txt import RepositorioTXT
from presentacion.consola import ConsolaTaller6


@pytest.fixture
def servicio(tmp_path: Path) -> ServicioGestionEscolar:
    """Crea un servicio aislado con archivo temporal."""
    repositorio = RepositorioTXT(tmp_path / "taller6.txt")
    return ServicioGestionEscolar(repositorio=repositorio)


def test_registrar_colegio_publico_y_privado_aplica_polimorfismo(
    servicio: ServicioGestionEscolar,
) -> None:
    """Verifica que cada colegio responda distinto al mismo mensaje."""
    colegio_publico = servicio.registrar_colegio("Institución Central", "PUBLICO")
    colegio_privado = servicio.registrar_colegio("Colegio Innovador", "PRIVADO")

    assert colegio_publico.tipo() == "PUBLICO"
    assert colegio_privado.tipo() == "PRIVADO"
    assert colegio_publico.costo_base_matricula() == 50000
    assert colegio_privado.costo_base_matricula() == 150000


def test_registrar_alumno_becado_modifica_matricula_sin_condicionales(
    servicio: ServicioGestionEscolar,
) -> None:
    """Verifica el cálculo polimórfico entre colegio y alumno."""
    colegio = servicio.registrar_colegio("Colegio Nuevo Horizonte", "PRIVADO")
    alumno_regular = servicio.registrar_alumno(
        colegio_id=colegio.identificador,
        nombre="Laura",
        edad=15,
        grado="10A",
        perfil="REGULAR",
    )
    alumno_becado = servicio.registrar_alumno(
        colegio_id=colegio.identificador,
        nombre="Mateo",
        edad=16,
        grado="11B",
        perfil="BECADO",
    )

    assert colegio.calcular_matricula(alumno_regular) == 150000
    assert colegio.calcular_matricula(alumno_becado) == 75000


def test_registrar_alumno_en_colegio_inexistente_lanza_error(
    servicio: ServicioGestionEscolar,
) -> None:
    """Valida el manejo de errores del caso de uso."""
    with pytest.raises(ValueError, match="No existe un colegio"):
        servicio.registrar_alumno(
            colegio_id="COL-999",
            nombre="Sara",
            edad=14,
            grado="9A",
            perfil="REGULAR",
        )


@pytest.mark.parametrize(
    ("nombre", "edad", "grado"),
    [
        ("", 14, "8A"),
        ("Pedro", 0, "8A"),
        ("Pedro", 14, ""),
    ],
)
def test_creacion_de_alumno_con_datos_invalidos_falla(
    nombre: str, edad: int, grado: str
) -> None:
    """Cubre casos de borde y validación."""
    with pytest.raises(ValueError):
        FabricaAlumnos.crear(
            perfil="REGULAR",
            identificador="ALU-001",
            nombre=nombre,
            edad=edad,
            grado=grado,
        )


def test_roundtrip_txt_conserva_tipos_concretos(
    servicio: ServicioGestionEscolar,
) -> None:
    """Garantiza que el archivo TXT restaure las subclases correctas."""
    colegio_publico = servicio.registrar_colegio("Escuela Rural", "PUBLICO")
    colegio_privado = servicio.registrar_colegio("Colegio Bilingüe", "PRIVADO")
    servicio.registrar_alumno(
        colegio_id=colegio_publico.identificador,
        nombre="Ana",
        edad=13,
        grado="7A",
        perfil="REGULAR",
    )
    servicio.registrar_alumno(
        colegio_id=colegio_privado.identificador,
        nombre="Luis",
        edad=17,
        grado="11C",
        perfil="BECADO",
    )
    servicio.guardar_datos()

    colegios = servicio.cargar_datos()

    assert [colegio.tipo() for colegio in colegios] == ["PUBLICO", "PRIVADO"]
    assert [colegio.alumnos[0].perfil() for colegio in colegios] == [
        "REGULAR",
        "BECADO",
    ]


def test_repositorio_txt_rechaza_alumno_huerfano(tmp_path: Path) -> None:
    """Protege la integridad de la relación colegio-alumno."""
    ruta_archivo = tmp_path / "datos.txt"
    ruta_archivo.write_text(
        "[COLEGIOS]\nPUBLICO|COL-001|Colegio Base\n\n[ALUMNOS]\n"
        "REGULAR|ALU-001|COL-999|Inconsistente|14|8A\n",
        encoding="utf-8",
    )
    repositorio = RepositorioTXT(ruta_archivo)

    with pytest.raises(ValueError, match="colegio inexistente"):
        repositorio.cargar_colegios()


def test_factorias_rechazan_tipos_no_soportados() -> None:
    """Cubre el error de discriminadores inválidos."""
    with pytest.raises(ValueError, match="Tipo de colegio no soportado"):
        FabricaColegios.crear("MIXTO", "COL-001", "Colegio X")

    with pytest.raises(ValueError, match="Perfil de alumno no soportado"):
        FabricaAlumnos.crear("MONITOR", "ALU-001", "Luisa", 15, "10A")


def test_servicio_genera_identificadores_ignorando_formatos_invalidos() -> None:
    """Verifica la generación robusta de identificadores consecutivos."""
    assert (
        ServicioGestionEscolar._siguiente_identificador(
            "ALU",
            ["ALU-XYZ", "OTRO-001", "ALU-002"],
        )
        == "ALU-003"
    )


def test_consola_inicializar_sin_datos_informa_sesion_nueva(
    servicio: ServicioGestionEscolar,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """Cubre la inicialización cuando no existe archivo persistido."""
    consola = ConsolaTaller6(servicio)

    consola.inicializar()

    salida = capsys.readouterr().out
    assert "No se encontraron datos previos" in salida


def test_consola_inicializar_con_datos_carga_archivo(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """Cubre la inicialización cuando sí existen datos persistidos."""
    repositorio = RepositorioTXT(tmp_path / "taller6.txt")
    servicio = ServicioGestionEscolar(repositorio)
    colegio = servicio.registrar_colegio("Colegio Guardado", "PUBLICO")
    servicio.registrar_alumno(colegio.identificador, "Ana", 14, "8A", "REGULAR")
    servicio.guardar_datos()

    consola = ConsolaTaller6(ServicioGestionEscolar(repositorio))
    consola.inicializar()

    salida = capsys.readouterr().out
    assert "Se cargaron los datos guardados" in salida


def test_consola_muestra_mensajes_cuando_no_hay_datos(
    servicio: ServicioGestionEscolar,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """Cubre los estados vacíos de la consola."""
    consola = ConsolaTaller6(servicio)

    consola._registrar_alumno()
    consola._mostrar_colegios()
    consola._mostrar_alumnos_por_colegio()
    consola._mostrar_resumen_matriculas()

    salida = capsys.readouterr().out
    assert "Debe registrar al menos un colegio" in salida
    assert "No hay colegios registrados" in salida
    assert "No existen matrículas para mostrar" in salida


def test_consola_muestra_mensaje_si_colegio_no_tiene_alumnos(
    servicio: ServicioGestionEscolar,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """Cubre la consulta de un colegio sin alumnos asociados."""
    colegio = servicio.registrar_colegio("Colegio Sin Alumnos", "PUBLICO")
    consola = ConsolaTaller6(servicio)
    monkeypatch.setattr("builtins.input", lambda _: colegio.identificador)

    consola._mostrar_alumnos_por_colegio()

    salida = capsys.readouterr().out
    assert "todavía no tiene alumnos registrados" in salida


def test_consola_ejecuta_flujo_principal(
    servicio: ServicioGestionEscolar,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """Ejecuta un flujo completo del menú principal."""
    consola = ConsolaTaller6(servicio)
    entradas = iter(
        [
            "1",
            "Colegio Integral",
            "1",
            "2",
            "COL-001",
            "Laura",
            "15",
            "10A",
            "2",
            "3",
            "4",
            "COL-001",
            "5",
            "6",
            "7",
            "9",
            "8",
        ]
    )
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    consola.ejecutar()

    salida = capsys.readouterr().out
    assert "Colegio registrado correctamente" in salida
    assert "Alumno registrado correctamente" in salida
    assert "Resumen de matrículas" in salida
    assert "Los datos fueron guardados correctamente" in salida
    assert "La opción seleccionada no es válida" in salida
    assert "Saliendo de la aplicación." in salida


def test_validaciones_estaticas_de_consola(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Cubre validaciones de menú y lectura numérica."""
    with pytest.raises(ValueError, match="Debe seleccionar 1 para público"):
        ConsolaTaller6._mapear_tipo_colegio("5")

    with pytest.raises(ValueError, match="Debe seleccionar 1 para regular"):
        ConsolaTaller6._mapear_perfil_alumno("8")

    monkeypatch.setattr("builtins.input", lambda _: "-2")
    with pytest.raises(ValueError, match="número entero positivo"):
        ConsolaTaller6._leer_entero_positivo("Edad: ")
