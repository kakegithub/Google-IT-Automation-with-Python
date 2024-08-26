def clothing_type(temp):
    if temp > 65:
        clothing = "T-Shirt"
    elif temp > 50 and temp <= 65:
        clothing = "Sweatshirt"
    elif temp > 32 and temp <= 50:
        clothing = "Jacket"
    else:
        clothing = "Heavy Coat"
    return clothing


print(clothing_type(72))  # Should print T-Shirt
print(clothing_type(55))  # Should print Sweatshirt
print(clothing_type(65))  # Should print Sweatshirt
print(clothing_type(50))  # Should print Jacket
print(clothing_type(45))  # Should print Jacket
print(clothing_type(32))  # Should print Heavy Coat
print(clothing_type(0))  # Should print Heavy Coat
############################################################################


def letter_translator(letter):
    if letter == "a":
        letter_position = 1
    elif letter == "b":
        letter_position = 2
    elif letter == "c":
        letter_position = 3
    elif letter == "d":
        letter_position = 4
    else:
        letter_position = "unknown"
    return letter_position


print(letter_translator("a"))  # Should print 1
print(letter_translator("b"))  # Should print 2
print(letter_translator("c"))  # Should print 3
print(letter_translator("d"))  # Should print 4
print(letter_translator("e"))  # Should print unknown
print(letter_translator("A"))  # Should print unknown
print(letter_translator(""))  # Should print unknown
###################################################################################


def make_positive(number):
    if number < 0:
        result = number * -1
    else:
        result = number
    return result


print(make_positive(-4))  # Should print 4
print(make_positive(0))  # Should print 0
print(make_positive(-0.25))  # Should print 0.25
print(make_positive(5))  # Should print 5
######################################################################################3
