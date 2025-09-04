########################################################################

# Ejemplo de ordenamiento de una lista de números
numbers = [4, 6, 2, 7, 1]
numbers.sort()  # Ordena la lista 'numbers' in-place (modifica la lista original)
print(numbers)  # Imprime la lista ordenada
# Output: [1, 2, 4, 6, 7]

########################################################################

# Ejemplo de ordenamiento de una lista de cadenas
names = ["Carlos", "Ray", "Alex", "Kelly"]
print(sorted(names))  # Imprime una nueva lista ordenada alfabéticamente (no modifica la lista original)
# Output: ['Alex', 'Carlos', 'Kelly', 'Ray']
print(names)  # Imprime la lista original sin modificar
# Output: ['Carlos', 'Ray', 'Alex', 'Kelly']
print(
    sorted(names, key=len)
)  # Imprime una nueva lista ordenada por la longitud de las cadenas
# Output: ['Ray', 'Alex', 'Kelly', 'Carlos']

##########################################################################


def get_event_date(event):
    """
    Función auxiliar para obtener la fecha de un evento.
    (Esta función no está definida en el código proporcionado, pero se asume que existe y devuelve la fecha del evento)
    """
    return event.date


def current_users(events):
    """
    Analiza una lista de eventos para determinar los usuarios actuales en cada máquina.

    Args:
        events (list): Una lista de objetos 'event' con atributos 'machine', 'user' y 'type' ('login' o 'logout').

    Returns:
        dict: Un diccionario donde las claves son los nombres de las máquinas y los valores son conjuntos de usuarios actualmente conectados a esa máquina.
    """
    events.sort(
        key=get_event_date
    )  # Ordena los eventos por fecha (asumiendo que 'get_event_date' es una función definida en otro lugar)
    machines = {}  # Inicializa un diccionario para almacenar los usuarios actuales por máquina
    for event in events:  # Itera sobre cada evento en la lista ordenada
        if (
            event.machine not in machines
        ):  # Si la máquina no está en el diccionario, crea una entrada para ella
            machines[event.machine] = (
                set()
            )  # Inicializa un conjunto vacío para los usuarios de esa máquina
        if (
            event.type == "login"
        ):  # Si el evento es un inicio de sesión, agrega el usuario al conjunto de la máquina
            machines[event.machine].add(event.user)
        elif (
            event.type == "logout"
        ):  # Si el evento es un cierre de sesión, elimina el usuario del conjunto de la máquina
            machines[event.machine].remove(event.user)
    return machines  # Devuelve el diccionario con los usuarios actuales por máquina


###################################################################################


def generate_report(machines):
    """
    Genera un informe de los usuarios actuales en cada máquina.

    Args:
        machines (dict): Un diccionario donde las claves son los nombres de las máquinas y los valores son conjuntos de usuarios actualmente conectados a esa máquina.
    """
    for (
        machine,
        users,
    ) in (
        machines.items()
    ):  # Itera sobre cada máquina y su conjunto de usuarios en el diccionario
        if (
            len(users) > 0
        ):  # Si hay usuarios conectados a la máquina, genera un informe
            user_list = ", ".join(
                users
            )  # Convierte el conjunto de usuarios en una cadena separada por comas
            print(
                "{}: {}".format(machine, user_list)
            )  # Imprime el nombre de la máquina y la lista de usuarios


##################################################################################
