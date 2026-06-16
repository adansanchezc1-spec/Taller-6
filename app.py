"""Punto de entrada del Taller 6."""

from pathlib import Path

from aplicacion.servicio_gestion_escolar import ServicioGestionEscolar
from infraestructura.repositorio_txt import RepositorioTXT
from presentacion.consola import ConsolaTaller6


def main() -> None:
    """Inicializa la aplicación de consola."""
    ruta_archivo = Path("data") / "taller6.txt"
    repositorio = RepositorioTXT(ruta_archivo=ruta_archivo)
    servicio = ServicioGestionEscolar(repositorio=repositorio)
    consola = ConsolaTaller6(servicio=servicio)
    consola.inicializar()
    consola.ejecutar()


if __name__ == "__main__":
    main()
