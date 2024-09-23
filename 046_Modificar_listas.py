##################################################################################################


# Añadir un elemento a la lista

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kiwi")
print(fruits)

# ['Pineapple', 'Banana', 'Apple', 'Melon', 'Kiwi']


#################################################################################################


# Insertar un elemento en la lista

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
print(fruits)

# ['Orange', 'Pineapple', 'Banana', 'Apple', 'Melon']


####################################################################################################


# Insertar elementos en la lista

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
print(fruits)

# ['Orange', 'Pineapple', 'Banana', 'Apple', 'Melon', 'Peach']


####################################################################################################


# Remover elementos en la lista

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
fruits.remove("Melon")
print(fruits)

# ['Orange', 'Pineapple', 'Banana', 'Apple', 'Peach']


#######################################################################################################


# fruits = ["Pineapple", "Banana", "Apple", "Melon"]
# fruits.remove("Pear")
# This will throw an error


#########################################################################################################


# Removiendo elemento en una posicion especifica de la lista

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
fruits.remove("Melon")
fruits.pop(3)
print(fruits)

# ['Orange', 'Pineapple', 'Banana', 'Peach']


##########################################################################################################

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
fruits.remove("Melon")
fruits.pop(3)
fruits[2] = "Strawberry"
print(fruits)


##############################################################################################################
