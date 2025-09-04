"""
Demostración de principios de reutilización de código:
- Evitar duplicación: extraer la lógica común a funciones reutilizables.
- Separar la lógica de negocio (cálculo) de la presentación (formato/impresión).
- Usar f-strings por legibilidad y seguridad.

Este módulo calcula e imprime el 'número de la suerte' para uno o varios nombres.
"""

from typing import Iterable


def lucky_number(name: str) -> int:
    """
    Calcula el 'número de la suerte' a partir del nombre.

    Regla: número = len(name) * 9

    Parámetros:
        name (str): Nombre de la persona. Puede ser cadena vacía.

    Retorna:
        int: Número de la suerte calculado.
    """
    return len(name) * 9


def format_lucky_greeting(name: str) -> str:
    """
    Construye el mensaje con el saludo y el número de la suerte.
    Mantiene la responsabilidad de solo dar formato (no imprime).
    """
    number = lucky_number(name)
    return f"Hello {name}. Your lucky number is {number}"


def print_lucky_greeting(name: str) -> None:
    """
    Imprime en consola el saludo con el número de la suerte para un nombre.
    Separa la E/S (efecto secundario) de la lógica pura.
    """
    print(format_lucky_greeting(name))


def print_greetings(names: Iterable[str]) -> None:
    """
    Imprime en consola el saludo con el número de la suerte para cada nombre.
    Evita duplicación al reutilizar la misma función en un bucle.
    """
    for name in names:
        print_lucky_greeting(name)


def main() -> None:
    """
    Punto de entrada del script. Define una lista de nombres y los procesa.
    """
    nombres = ["Kay", "Cameron"]
    print_greetings(nombres)


if __name__ == "__main__":
    # Main guard: permite importar este módulo sin ejecutar código.
    main()
