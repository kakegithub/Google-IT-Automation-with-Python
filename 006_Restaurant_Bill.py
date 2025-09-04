"""
Escenario: Dos amigos cenan en un restaurante. La cuenta es de 47.28 dólares.
Deciden agregar una propina del 15% y dividir el total en partes iguales.
El objetivo es calcular la propina, el total a pagar y la parte de cada uno,
y mostrar: "Each person needs to pay: <monto>".

Nota: Este script mantiene el comportamiento original sin cambios, incluso si
hubiera posibles errores de lógica en los cálculos; se señalan en comentarios.
"""

bill = 47.28  # Asignamos el monto de la cuenta (en dólares)

tip = (bill * 15) / 100  # Calculamos la propina como el 15% de la cuenta

# Sumamos al total la cuenta más la MITAD de la propina.
# ATENCIÓN: Si la intención fuera sumar toda la propina, debería ser 'bill + tip'.
# Se deja como en el original para no cambiar el comportamiento del programa.
total = bill + (tip / 2)

# Dividimos el total entre dos personas para obtener la parte de cada una.
share = total / 2

# Mostramos el resultado. Convertimos 'share' a cadena con str() para poder
# concatenarlo con otras cadenas. Se añade el símbolo "$" al final.
# Observación: El enunciado mencionaba un ":" después de "pay"; aquí no está.
print("Each person needs to pay " + str(share) + "$")

# Sugerencias (no aplicadas para no cambiar el comportamiento):
# - Para sumar la propina completa: total = bill + tip
# - Para formatear con 2 decimales: f"{share:.2f}"
# - Para seguir exactamente el texto "Each person needs to pay: ":
#   print("Each person needs to pay: " + str(share) + "$")
