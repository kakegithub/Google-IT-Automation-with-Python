import shutil  # Importa el módulo shutil para operaciones de alto nivel con archivos y directorios
import psutil  # Importa el módulo psutil para obtener información del sistema y los procesos

# Obtiene el uso del disco para la partición raíz ("/")
du = shutil.disk_usage("/")

# Imprime la información del uso del disco
print(du)  # Imprime la información sin formato (en bytes)
print(f"Total: {du.total / (1024 ** 3):.2f} GB")  # Imprime el espacio total en GB, formateado a 2 decimales
print(f"Used: {du.used / (1024 ** 3):.2f} GB")  # Imprime el espacio usado en GB, formateado a 2 decimales
print(f"Free: {du.free / (1024 ** 3):.2f} GB")  # Imprime el espacio libre en GB, formateado a 2 decimales
print(f"Percentage used: {du.used / du.total * 100:.2f}%")  # Imprime el porcentaje de espacio usado, formateado a 2 decimales

# Obtiene el porcentaje de uso de la CPU
psutil.cpu_percent(0.1)  # Llama a la función para obtener el uso de la CPU (con un breve retraso inicial)

# Imprime el uso de la CPU cada segundo durante 10 segundos
for i in range(10):
    print(f"CPU usage at {i+1} seconds: {psutil.cpu_percent(interval=1)}%")  # Imprime el uso de la CPU, con un intervalo de 1 segundo

# Imprime información adicional del sistema
print(f"CPU count: {psutil.cpu_count(logical=True)}")  # Imprime el número de CPUs lógicas
print(f"Memory usage: {psutil.virtual_memory().percent}%")  # Imprime el porcentaje de uso de la memoria virtual
print(f"Swap usage: {psutil.swap_memory().percent}%")  # Imprime el porcentaje de uso del espacio de intercambio (swap)
