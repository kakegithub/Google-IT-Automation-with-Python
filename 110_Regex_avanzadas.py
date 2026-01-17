
# Alteraciones
r"location.*(London|Berlin|Madrid)"
# Esta línea de código coincidirá con la cadena de texto location is London, location is Berlin, o location is Madrid.


# Coincidencia sólo al principio o al final
r” ^ My name is (\w+)”
# Esta línea de código coincidirá con My name is Asha pero no con Hello. My name is Asha.



# Rangos de caracteres
# r”[A-Z] Esto coincidirá con una sola letra mayúscula.
# r”[0-9$-,.] Coincidirá con cualquiera de los dígitos del cero al nueve, o con el símbolo del dólar, el guión, la coma o el punto.

r”([0-9]{3}-[0-9]{3}-[0-9]{4})”
# Esta línea de código coincidirá con un número de teléfono de EE.UU. como 888-123-7612.


# Referencias
>>> re.sub(r”([A-Z])\.\s+(\w+)”, r”Ms. \2”, “A. Weber and B. Bellmas have joined the team.”)
        #    Esta línea de código producirá Ms. Weber and Ms. Bellmas have joined the team.


# Lookahead
r”(Test\d)-(?=Passed)” y la cadena “Test1-Passed, Test2-Passed, Test3-Failed, Test4-Passed, Test5-Failed”
# Test1, Test2, Test4

