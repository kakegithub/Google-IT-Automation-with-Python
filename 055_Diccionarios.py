# Habilidades de codificación

# Habilidad Grupo 1

#     Iterar sobre los pares clave y valor de un diccionario utilizando un bucle for con el método dictionary.items() para calcular la suma de los valores de un diccionario.

# This function returns the total time, with minutes represented as
# decimals (example: 1 hour 30 minutes = 1.5), for all end user time
# spent accessing a server in a given day.


def sum_server_use_time(Server):

    # Initialize the variable as a float data type, which will be used
    # to hold the sum of the total hours and minutes of server usage by
    # end users in a day.
    total_use_time = 0.0

    # Iterate through the "Server" dictionary’s key and value items
    # using a for loop.
    for key, value in Server.items():

        # For each end user key, add the associated time value to the
        # total sum of all end user use time.
        total_use_time += Server[key]

    # Round the return value and limit to 2 decimal places.
    return round(total_use_time, 2)


FileServer = {
    "EndUser1": 2.25,
    "EndUser2": 4.5,
    "EndUser3": 1,
    "EndUser4": 3.75,
    "EndUser5": 0.6,
    "EndUser6": 8,
}

print(sum_server_use_time(FileServer))  # Should print 20.1


##########################################################################################################


# Grupo de destrezas 2

#     Concatene un valor, una cadena y la clave de cada elemento del diccionario y añádalos al final de una nueva lista[ ] mediante el método list.append(x).

#     Iterar sobre claves con múltiples valores de un diccionario utilizando bucles for anidados con el método dictionary.items().

# This function receives a dictionary, which contains common employee
# last names as keys, and a list of employee first names as values.
# The function generates a new list that contains each employees’ full
# name (First_name Last_Name). For example, the key "Garcia" with the
# values ["Maria", "Hugo", "Lucia"] should be converted to a list
# that contains ["Maria Garcia", "Hugo Garcia", "Lucia Garcia"].


def list_full_names(employee_dictionary):
    # Initialize the "full_names" variable as a list data type using
    # empty [] square brackets.
    full_names = []

    # The outer for loop iterates through each "last_name" key and
    # associated "first_name" values, in the "employee_dictionary" items.
    for last_name, first_names in employee_dictionary.items():

        # The inner for loop iterates over each "first_name" value in
        # the list of "first_names" for one "last_name" key at a time.
        for first_name in first_names:

            # Append the new "full_names" list with the "first_name" value
            # concatenated with a space " ", and the key "last_name".
            full_names.append(first_name + " " + last_name)

    # Return the new "full_names" list once the outer for loop has
    # completed all iterations.
    return full_names


print(
    list_full_names(
        {
            "Ali": ["Muhammad", "Amir", "Malik"],
            "Devi": ["Ram", "Amaira"],
            "Chen": ["Feng", "Li"],
        }
    )
)
# Should print ['Muhammad Ali', 'Amir Ali', 'Malik Ali', 'Ram Devi', 'Amaira Devi', 'Feng Chen', 'Li Chen']

##############################################################################################################################

# Grupo de destrezas 3

#     Utilizar la operación dictionary[key] = value para asociar un valor a una clave de un diccionario.

#     Iterar sobre claves con múltiples valores de un diccionario, utilizando bucles for anidados y una sentencia if, y el método dictionary.items().

#     Utilice el método dictionary[key].append(value) para añadir la clave, una cadena y la clave de cada elemento del diccionario.

# This function receives a dictionary, which contains resource
# categories (keys) with a list of available resources (values) for a
# company’s IT Department. The resources belong to multiple categories.
# The function should reverse the keys and values to show which
# categories (values) each resource (key) belongs to.


def invert_resource_dict(resource_dictionary):
    # Initialize a "new_dictionary" variable as a dict data type using
    # empty {} curly brackets.
    new_dictionary = {}
    # The outer for loop iterates through each "resource_group" and
    # associated "resources" in the "resource_dictionary" items.
    for resource_group, resources in resource_dictionary.items():
        # The inner for loop iterates over each "resource" value in
        # the list of "resources" for one "resource_group" key at a time.
        for resource in resources:
            # The if-statement checks if the current "resource" value has
            # been appended as a key to the "new_dictionary" yet.
            if resource in new_dictionary:
                # If True, then append the "resource_group" as a value to the
                # "resource", which is now the key.
                new_dictionary[resource].append(resource_group)
            # If False (else), then add the "resource" as a new key with the
            # "resource_group" as a value for that key.
            else:
                new_dictionary[resource] = [resource_group]
    # Return the new dictionary once the outer for loop has completed
    # all iterations.
    return new_dictionary


print(
    invert_resource_dict(
        {
            "Hard Drives": ["IDE HDDs", "SCSI HDDs"],
            "PC Parts": [
                "IDE HDDs",
                "SCSI HDDs",
                "High-end video cards",
                "Basic video cards",
            ],
            "Video Cards": ["High-end video cards", "Basic video cards"],
        }
    )
)
# Should print {'IDE HDDs': ['Hard Drives', 'PC Parts'], 'SCSI HDDs': ['Hard Drives', 'PC Parts'], 'High-end video cards': ['PC Parts', 'Video Cards'], 'Basic video cards': ['PC Parts', 'Video Cards']}

################################################################################################################################################


# La función email_list recibe un diccionario, que contiene nombres de dominio como claves, y una lista de usuarios como valores. Rellene los espacios en blanco para generar una lista que contenga direcciones de correo electrónico completas (por ejemplo, diana.prince@gmail.com).


def email_list(domains):
    emails = []
    for domain, users in domains.items():
        for user in users:
            emails.append(f"{user}@{domain}")
    return emails


print(
    email_list(
        {
            "gmail.com": ["clark.kent", "diana.prince", "peter.parker"],
            "yahoo.com": ["barbara.gordon", "jean.grey"],
            "hotmail.com": ["bruce.wayne"],
        }
    )
)
# ['clark.kent@gmail.com', 'diana.prince@gmail.com', 'peter.parker@gmail.com', 'barbara.gordon@yahoo.com', 'jean.grey@yahoo.com', 'bruce.wayne@hotmail.com']

############################################################################################################################################3

# La función groups_per_user recibe un diccionario, que contiene los nombres de los grupos con la lista de usuarios. Los usuarios pueden pertenecer a varios grupos. Rellena los espacios en blanco para devolver un diccionario con los usuarios como claves y una lista de sus grupos como valores.


def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group, users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
            # If the user is not already in the dictionary, add them
            if user not in user_groups:
                user_groups[user] = []
            # Add the group to the user's list
            user_groups[user].append(group)
    return user_groups


print(
    groups_per_user(
        {
            "local": ["admin", "userA"],
            "public": ["admin", "userB"],
            "administrator": ["admin"],
        }
    )
)

################################################################################################################

# El método dict.update actualiza un diccionario con los elementos procedentes del otro diccionario, de forma que se sustituyen las entradas existentes y se añaden otras nuevas. ¿Cuál es el contenido del diccionario "armario" al final del siguiente código?

wardrobe = {"shirt": ["red", "blue", "white"], "jeans": ["blue", "black"]}
new_items = {"jeans": ["white"], "scarf": ["yellow"], "socks": ["black", "brown"]}
wardrobe.update(new_items)

#
###############################################################################################################3

# La función sumar_precios devuelve el precio total de todos los comestibles del diccionario. Rellene los espacios en blanco para completar esta función.


def add_prices(basket):
    # Initialize the variable that will be used for the calculation
    total = 0
    # Iterate through the dictionary items
    for price in basket.values():
        # Add each price to the total calculation
        # Hint: how do you access the values of
        # dictionary items?
        total += price
    # Limit the return value to 2 decimal places
    return round(total, 2)


groceries = {
    "bananas": 1.56,
    "apples": 2.50,
    "oranges": 0.99,
    "bread": 4.59,
    "coffee": 6.99,
    "milk": 3.39,
    "eggs": 2.98,
    "cheese": 5.44,
}

print(add_prices(groceries))  # Should print 28.44

# 28.44
