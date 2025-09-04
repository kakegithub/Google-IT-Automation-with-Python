# Modificar listas: append, insert, remove, pop y asignación por índice

# -----------------------------------------------------------------------------
# Añadir un elemento al final de la lista con append()
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kiwi")
print(fruits)
# ['Pineapple', 'Banana', 'Apple', 'Melon', 'Kiwi']

# -----------------------------------------------------------------------------
# Insertar un elemento en una posición específica con insert(pos, valor)
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")  # Inserta al inicio
print(fruits)
# ['Orange', 'Pineapple', 'Banana', 'Apple', 'Melon']

# -----------------------------------------------------------------------------
# Insertar fuera del rango: se inserta al final si el índice es mayor que la longitud
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")  # 25 > len(fruits) -> se añade al final
print(fruits)
# ['Orange', 'Pineapple', 'Banana', 'Apple', 'Melon', 'Peach']

# -----------------------------------------------------------------------------
# Remover un elemento por valor con remove(valor) (elimina la primera coincidencia)
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
fruits.remove("Melon")  # Elimina 'Melon' si existe; ValueError si no está
print(fruits)
# ['Orange', 'Pineapple', 'Banana', 'Apple', 'Peach']

# Nota: intentar eliminar un valor que no existe provoca ValueError
# Ejemplo (no ejecutar):
# fruits = ["Pineapple", "Banana", "Apple", "Melon"]
# fruits.remove("Pear")  # ValueError: list.remove(x): x not in list

# -----------------------------------------------------------------------------
# Remover por posición con pop(indice) (retorna el elemento eliminado)
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
fruits.remove("Melon")
fruits.pop(3)  # Elimina el elemento en el índice 3 ('Apple')
print(fruits)
# ['Orange', 'Pineapple', 'Banana', 'Peach']

# -----------------------------------------------------------------------------
# Reemplazar un elemento por índice (asignación)
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
fruits.remove("Melon")
fruits.pop(3)
fruits[2] = "Strawberry"  # Sustituye 'Banana' por 'Strawberry'
print(fruits)
# ['Orange', 'Pineapple', 'Strawberry', 'Peach']
