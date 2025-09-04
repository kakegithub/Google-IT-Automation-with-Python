##################################################################################
# Función para obtener la fecha de un evento
def get_event_date(event):
    """
    Obtiene la fecha de un evento.
    Args:
        event: El evento del cual se quiere obtener la fecha.
    Returns:
        La fecha del evento.
    """
    return event.date


# Función para determinar los usuarios actuales en cada máquina
def current_users(events):
    """
    Determina los usuarios actuales en cada máquina basándose en los eventos de inicio y cierre de sesión.
    Args:
        events: Una lista de objetos Event que representan los eventos de inicio y cierre de sesión.
    Returns:
        Un diccionario donde las claves son los nombres de las máquinas y los valores son conjuntos de usuarios actualmente conectados a esa máquina.
    """
    events.sort(key=get_event_date)  # Ordena los eventos por fecha
    machines = {}  # Inicializa un diccionario para almacenar los usuarios por máquina
    for event in events:  # Itera sobre cada evento
        if event.machine not in machines:  # Si la máquina no está en el diccionario
            machines[event.machine] = set()  # Inicializa un conjunto para esa máquina
        if event.type == "login":  # Si el evento es un inicio de sesión
            machines[event.machine].add(event.user)  # Agrega el usuario a la máquina
        elif event.type == "logout":  # Si el evento es un cierre de sesión
            machines[event.machine].remove(event.user)  # Elimina el usuario de la máquina
    return machines  # Devuelve el diccionario de máquinas y usuarios


# Función para generar un informe de los usuarios actuales en cada máquina
def generate_report(machines):
    """
    Genera un informe de los usuarios actuales en cada máquina.
    Args:
        machines: Un diccionario donde las claves son los nombres de las máquinas y los valores son conjuntos de usuarios actualmente conectados a esa máquina.
    """
    for machine, users in machines.items():  # Itera sobre cada máquina y sus usuarios
        if len(users) > 0:  # Si hay usuarios en la máquina
            user_list = ", ".join(users)  # Crea una lista de usuarios separada por comas
            print("{}: {}".format(machine, user_list))  # Imprime el informe


# Clase para representar un evento
class Event:
    """
    Clase para representar un evento.
    """

    def __init__(self, event_date, event_type, machine_name, user):
        """
        Inicializa un objeto Event.
        Args:
            event_date: La fecha del evento.
            event_type: El tipo de evento (login o logout).
            machine_name: El nombre de la máquina.
            user: El usuario asociado con el evento.
        """
        self.date = event_date  # Asigna la fecha del evento
        self.type = event_type  # Asigna el tipo de evento
        self.machine = machine_name  # Asigna el nombre de la máquina
        self.user = user  # Asigna el usuario


# Lista de eventos
events = [
    Event("2020-01-21 12:45:46", "login", "myworkstation.local", "jordan"),
    Event("2020-01-22 15:53:42", "logout", "webserver.local", "jordan"),
    Event("2020-01-21 18:53:21", "login", "webserver.local", "lane"),
    Event("2020-01-22 10:25:34", "logout", "myworkstation.local", "jordan"),
    Event("2020-01-21 08:20:01", "login", "webserver.local", "jordan"),
    Event("2020-01-23 11:24:35", "login", "mailserver.local", "chris"),
]

# Obtiene los usuarios actuales
users = current_users(events)
print(users)  # Imprime el diccionario de usuarios actuales

# Genera el informe
generate_report(users)  # Genera el informe de usuarios actuales
