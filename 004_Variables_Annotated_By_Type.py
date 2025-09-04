"""
Ejemplos de variables anotadas por tipo (type hints) en Python.
Estas anotaciones ayudan a herramientas de análisis estático, editores y lectores
humanos a entender el tipo esperado de cada variable, sin afectar la ejecución.

Nota: A partir de Python 3.9 se puede usar la sintaxis nativa de genéricos
(list[int], dict[str, int], etc.). Aquí se usa el módulo typing para mantener
compatibilidad con versiones anteriores.
"""

import typing

# Variable de tipo str (cadena de texto)
z: str = "Hello, world!"

# Variable de tipo int (entero)
x: int = 10

# Variable de tipo float (número de punto flotante)
y: float = 1.23

# Lista de enteros: typing.List[int]
list_of_numbers: typing.List[int] = [1, 2, 3]

# Tupla de exactamente tres enteros: typing.Tuple[int, int, int]
tuple_of_numbers: typing.Tuple[int, int, int] = (1, 2, 3)

# Diccionario con claves str y valores int: typing.Dict[str, int]
dictionary: typing.Dict[str, int] = {"key1": 1, "key2": 2}

# Conjunto (set) de enteros: typing.Set[int]
set_of_numbers: typing.Set[int] = {1, 2, 3}
