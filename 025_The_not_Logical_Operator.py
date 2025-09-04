# Operador lógico 'not': invierte (niega) un valor booleano

# Test Example 1:
# 2 * 3 = 6 y 6 > 6 es False, por lo tanto x es False
x = 2 * 3 > 6
print("The value of x is:")
print(x)

print()  # Imprime una línea en blanco

print("The inverse value of x is:")
print(not x)

print()
# Test Example 2:

# ¿Qué pasa al negar una afirmación que es False?
# En Python es más claro usar "!=" que "not a == b".

today = "Monday"
# "today != \"Tuesday\"" es True porque hoy no es martes
print(today != "Tuesday")

# Explicación:
# La variable today es "Monday", por lo que la comparación
# "today == \"Tuesday\"" sería False. Usando "not False" obtendríamos True.
# De forma más clara, se puede escribir como "today != \"Tuesday\"".
