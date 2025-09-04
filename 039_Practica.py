# Práctica: bucles while/for, rangos y formación de cadenas

# -----------------------------------------------------------------------------
# Contar de 2 en 2 hasta 12 con while (misma línea)
number = 2  # Inicializa la variable
while number <= 12:  # Condición del bucle
    print(number, end=" ")
    number += 2  # Incrementa de 2 en 2
print()  # Salto de línea tras la secuencia
# Debe imprimir: 2 4 6 8 10 12

# -----------------------------------------------------------------------------
# Contar de 2 en 2 hasta 12 con for y range (una línea por número)
for number in range(2, 12 + 1, 2):
    print(number)
# Debe imprimir:
# 2
# 4
# 6
# 8
# 10
# 12

# -----------------------------------------------------------------------------
# Contar cuántos números pares hay desde 0 hasta n (inclusive). 0 cuenta como par.

def even_numbers(n: int) -> int:
    """Retorna la cantidad de números pares en [0, n].

    Si n < 0, retorna 0 (no hay pares en el rango [0, n]).
    """
    count = 0
    current_number = 0
    while current_number <= n:
        if current_number % 2 == 0:
            count += 1
        current_number += 1
    return count


print(even_numbers(25))   # Debe imprimir 13
print(even_numbers(144))  # Debe imprimir 73
print(even_numbers(1000)) # Debe imprimir 501
print(even_numbers(0))    # Debe imprimir 1

# -----------------------------------------------------------------------------
# Tabla de multiplicar de start..stop (ambos inclusivos)

def multiplication_table(start: int, stop: int) -> None:
    """Imprime la tabla de multiplicar entre start y stop (inclusive)."""
    for x in range(start, stop + 1):  # bucle externo (filas)
        for y in range(start, stop + 1):  # bucle interno (columnas)
            print(str(x * y), end=" ")  # valor y espacio
        print()  # fin de fila -> salto de línea


multiplication_table(1, 3)
# Debe imprimir la tabla de multiplicar mostrada en el enunciado

# -----------------------------------------------------------------------------
# Cuenta regresiva hasta 0 devolviendo una cadena

def countdown(start: int) -> str:
    """Devuelve "Counting down to 0: n,n-1,...,0" o un mensaje si start == 0.

    Para start == 0 se retorna "Cannot count down to 0" según especificación.
    """
    x = start
    if x > 0:
        return_string = "Counting down to 0: "
        while x >= 0:
            return_string += str(x)
            if x > 0:
                return_string += ","
            x -= 1
    else:
        return_string = "Cannot count down to 0"
    return return_string


print(countdown(10))  # "Counting down to 0: 10,9,8,7,6,5,4,3,2,1,0"
print(countdown(2))   # "Counting down to 0: 2,1,0"
print(countdown(0))   # "Cannot count down to 0"

# -----------------------------------------------------------------------------
# Retornar todos los números entre minimum y maximum (inclusive) separados por espacios

def all_numbers(minimum: int, maximum: int) -> str:
    """Retorna "minimum minimum+1 ... maximum" (inclusive), separados por espacios."""
    return " ".join(str(x) for x in range(minimum, maximum + 1))


print(all_numbers(2, 6))   # Debe ser: 2 3 4 5 6
print(all_numbers(3, 10))  # Debe ser: 3 4 5 6 7 8 9 10
print(all_numbers(-1, 1))  # Debe ser: -1 0 1
print(all_numbers(0, 5))   # Debe ser: 0 1 2 3 4 5
print(all_numbers(0, 0))   # Debe ser: 0
