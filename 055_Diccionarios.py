# --- Habilidades de codificación ---

# --- Grupo de habilidades 1 ---
# Iterar sobre los pares clave y valor de un diccionario utilizando un bucle for con el método dictionary.items() para calcular la suma de los valores de un diccionario.

# Esta función devuelve el tiempo total, con los minutos representados como decimales (ejemplo: 1 hora 30 minutos = 1.5), para todo el tiempo que el usuario final pasa accediendo a un servidor en un día determinado.
def sum_server_use_time(Server):
    """
    Calcula el tiempo total de uso del servidor por los usuarios finales en un día.
    Args:
        Server (dict): Un diccionario donde las claves son los nombres de los usuarios y los valores son el tiempo de uso del servidor en horas.
    Returns:
        float: El tiempo total de uso del servidor redondeado a 2 decimales.
    """
    # Inicializar la variable como un tipo de datos float, que se utilizará para mantener la suma del total de horas y minutos de uso del servidor por los usuarios finales en un día.
    total_use_time = 0.0

    # Iterar a través de los elementos clave y valor del diccionario "Server" utilizando un bucle for.
    for key, value in Server.items():
        # Para cada clave de usuario final, añadir el valor de tiempo asociado a la suma total de todo el tiempo de uso del usuario final.
        total_use_time += value

    # Redondear el valor de retorno y limitar a 2 decimales.
    return round(total_use_time, 2)


FileServer = {
    "EndUser1": 2.25,
    "EndUser2": 4.5,
    "EndUser3": 1,
    "EndUser4": 3.75,
    "EndUser5": 0.6,
    "EndUser6": 8,
}

print(sum_server_use_time(FileServer))  # Debería imprimir 20.1

# --- Grupo de habilidades 2 ---
# Concatenar un valor, una cadena y la clave de cada elemento del diccionario y añadirlos al final de una nueva lista[] mediante el método list.append(x).
# Iterar sobre claves con múltiples valores de un diccionario utilizando bucles for anidados con el método dictionary.items().

# Esta función recibe un diccionario, que contiene apellidos comunes de empleados como claves, y una lista de nombres de empleados como valores.
# La función genera una nueva lista que contiene el nombre completo de cada empleado (Nombre Apellido).
# Por ejemplo, la clave "Garcia" con los valores ["Maria", "Hugo", "Lucia"] debe convertirse en una lista que contiene ["Maria Garcia", "Hugo Garcia", "Lucia Garcia"].
def list_full_names(employee_dictionary):
    """
    Genera una lista de nombres completos de empleados a partir de un diccionario de apellidos y nombres.
    Args:
        employee_dictionary (dict): Un diccionario donde las claves son los apellidos y los valores son listas de nombres.
    Returns:
        list: Una lista de nombres completos de empleados.
    """
    # Inicializar la variable "full_names" como un tipo de datos de lista utilizando corchetes [] vacíos.
    full_names = []

    # El bucle for externo itera a través de cada clave "last_name" y los valores "first_name" asociados, en los elementos "employee_dictionary".
    for last_name, first_names in employee_dictionary.items():
        # El bucle for interno itera sobre cada valor "first_name" en la lista de "first_names" para una clave "last_name" a la vez.
        for first_name in first_names:
            # Añadir la nueva lista "full_names" con el valor "first_name" concatenado con un espacio " ", y la clave "last_name".
            full_names.append(first_name + " " + last_name)

    # Devolver la nueva lista "full_names" una vez que el bucle for externo ha completado todas las iteraciones.
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
# Debería imprimir ['Muhammad Ali', 'Amir Ali', 'Malik Ali', 'Ram Devi', 'Amaira Devi', 'Feng Chen', 'Li Chen']

# --- Grupo de habilidades 3 ---
# Utilizar la operación dictionary[key] = value para asociar un valor a una clave de un diccionario.
# Iterar sobre claves con múltiples valores de un diccionario, utilizando bucles for anidados y una sentencia if, y el método dictionary.items().
# Utilice el método dictionary[key].append(value) para añadir la clave, una cadena y la clave de cada elemento del diccionario.

# Esta función recibe un diccionario, que contiene categorías de recursos (claves) con una lista de recursos disponibles (valores) para el Departamento de TI de una empresa.
# Los recursos pertenecen a múltiples categorías.
# La función debe invertir las claves y los valores para mostrar a qué categorías (valores) pertenece cada recurso (clave).
def invert_resource_dict(resource_dictionary):
    """
    Invierte un diccionario de recursos para mostrar a qué categorías pertenece cada recurso.
    Args:
        resource_dictionary (dict): Un diccionario donde las claves son las categorías de recursos y los valores son listas de recursos.
    Returns:
        dict: Un diccionario invertido donde las claves son los recursos y los valores son listas de categorías.
    """
    # Inicializar una variable "new_dictionary" como un tipo de datos dict utilizando corchetes {} rizados vacíos.
    new_dictionary = {}
    # El bucle for externo itera a través de cada "resource_group" y los "resources" asociados en los elementos "resource_dictionary".
    for resource_group, resources in resource_dictionary.items():
        # El bucle for interno itera sobre cada valor "resource" en la lista de "resources" para una clave "resource_group" a la vez.
        for resource in resources:
            # La sentencia if comprueba si el valor "resource" actual ha sido añadido como una clave al "new_dictionary" todavía.
            if resource in new_dictionary:
                # Si es True, entonces añadir el "resource_group" como un valor al "resource", que ahora es la clave.
                new_dictionary[resource].append(resource_group)
            # Si es False (else), entonces añadir el "resource" como una nueva clave con el "resource_group" como un valor para esa clave.
            else:
                new_dictionary[resource] = [resource_group]
    # Devolver el nuevo diccionario una vez que el bucle for externo ha completado todas las iteraciones.
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
# Debería imprimir {'IDE HDDs': ['Hard Drives', 'PC Parts'], 'SCSI HDDs': ['Hard Drives', 'PC Parts'], 'High-end video cards': ['PC Parts', 'Video Cards'], 'Basic video cards': ['PC Parts', 'Video Cards']}

# La función email_list recibe un diccionario, que contiene nombres de dominio como claves, y una lista de usuarios como valores. Rellene los espacios en blanco para generar una lista que contenga direcciones de correo electrónico completas (por ejemplo, diana.prince@gmail.com).
def email_list(domains):
    """
    Genera una lista de direcciones de correo electrónico completas a partir de un diccionario de dominios y usuarios.
    Args:
        domains (dict): Un diccionario donde las claves son los dominios y los valores son listas de usuarios.
    Returns:
        list: Una lista de direcciones de correo electrónico completas.
    """
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

# La función groups_per_user recibe un diccionario, que contiene los nombres de los grupos con la lista de usuarios. Los usuarios pueden pertenecer a varios grupos. Rellena los espacios en blanco para devolver un diccionario con los usuarios como claves y una lista de sus grupos como valores.
def groups_per_user(group_dictionary):
    """
    Genera un diccionario donde las claves son los usuarios y los valores son listas de grupos a los que pertenecen.
    Args:
        group_dictionary (dict): Un diccionario donde las claves son los nombres de los grupos y los valores son listas de usuarios.
    Returns:
        dict: Un diccionario donde las claves son los usuarios y los valores son listas de grupos.
    """
    user_groups = {}
    # Ir a través de group_dictionary
    for group, users in group_dictionary.items():
        # Ahora ir a través de los usuarios en el grupo
        for user in users:
            # Si el usuario no está ya en el diccionario, añadirlo
            if user not in user_groups:
                user_groups[user] = []
            # Añadir el grupo a la lista del usuario
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
# {'admin': ['local', 'public', 'administrator'], 'userA': ['local'], 'userB': ['public']}

# El método dict.update actualiza un diccionario con los elementos procedentes del otro diccionario, de forma que se sustituyen las entradas existentes y se añaden otras nuevas. ¿Cuál es el contenido del diccionario "armario" al final del siguiente código?
wardrobe = {"shirt": ["red", "blue", "white"], "jeans": ["blue", "black"]}
new_items = {"jeans": ["white"], "scarf": ["yellow"], "socks": ["black", "brown"]}
wardrobe.update(new_items)
print(wardrobe)
# {'shirt': ['red', 'blue', 'white'], 'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}

# La función sumar_precios devuelve el precio total de todos los comestibles del diccionario. Rellene los espacios en blanco para completar esta función.
def add_prices(basket):
    """
    Calcula el precio total de todos los comestibles en el diccionario.
    Args:
        basket (dict): Un diccionario donde las claves son los nombres de los comestibles y los valores son sus precios.
    Returns:
        float: El precio total de todos los comestibles redondeado a 2 decimales.
    """
    # Inicializar la variable que se utilizará para el cálculo
    total = 0
    # Iterar a través de los elementos del diccionario
    for price in basket.values():
        # Añadir cada precio al cálculo total
        # Pista: ¿cómo se accede a los valores de los elementos del diccionario?
        total += price
    # Limitar el valor de retorno a 2 decimales
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

print(add_prices(groceries))  # Debería imprimir 28.44
