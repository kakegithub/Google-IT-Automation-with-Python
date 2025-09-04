# Comparaciones lexicográficas (Unicode) con >= y <= sobre cadenas
# Se compara letra a letra por su valor Unicode hasta encontrar una diferencia.

var1 = "my computer" >= "my chair"   # True: tras "my ", 'o'(111) > 'h'(104)
var2 = "Spring" <= "Winter"           # True: 'S'(83) <= 'W'(87)
var3 = "pineapple" >= "pineapple"     # True: cadenas idénticas; se cumple por igualdad

print("Is \"my computer\" greater than or equal to \"my chair\"? Result: ", var1)
print("Is \"Spring\" less than or equal to \"Winter\"? Result: ", var2)
print("Is \"pineapple\" greater than or equal to \"pineapple\"? Result: ", var3)
