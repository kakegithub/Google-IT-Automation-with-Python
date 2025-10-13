#!/usr/bin/env python3
import csv


def read_employees(csv_file_location):
    """
    Lee un archivo CSV de empleados y lo convierte en una lista de diccionarios.

    Args:
        csv_file_location (str): La ruta al archivo CSV.

    Returns:
        list: Una lista de diccionarios, donde cada uno es un empleado.
    """
    # Registra un "dialecto" para manejar espacios extra después de las comas.
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)

    try:
        # El bloque 'with' asegura que el archivo se cierre automáticamente.
        with open(csv_file_location, mode='r', encoding='utf-8') as employee_file:
            # DictReader convierte cada fila en un diccionario.
            reader = csv.DictReader(employee_file, dialect='empDialect')
            # Convierte el objeto reader en una lista y la devuelve.
            return list(reader)
    except FileNotFoundError:
        print(
            f"Error: El archivo no se encontró en la ruta '{csv_file_location}'")
        return []


def process_data(employee_list):
    """
    Procesa la lista de empleados para contar cuántos hay por departamento.

    Args:
        employee_list (list): Una lista de diccionarios de empleados.

    Returns:
        dict: Un diccionario con el recuento de empleados por departamento.
    """
    department_data = {}
    # Itera sobre la lista de empleados UNA SOLA VEZ para mayor eficiencia.
    for employee_data in employee_list:
        department = employee_data.get('Department')
        # Incrementa el contador para ese departamento.
        # .get(department, 0) devuelve 0 si el departamento aún no existe en el diccionario.
        department_data[department] = department_data.get(department, 0) + 1
    return department_data


def write_report(dictionary, report_file):
    """
    Escribe un diccionario en un archivo de reporte, ordenado por clave.

    Args:
        dictionary (dict): El diccionario a escribir.
        report_file (str): La ruta al archivo de reporte de salida.
    """
    # Abre el archivo en modo escritura ('w').
    with open(report_file, "w") as f:
        # Itera sobre las claves del diccionario ordenadas alfabéticamente.
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')
        # No es necesario f.close() cuando se usa 'with'.


def main():
    """
    Función principal que orquesta la lectura, procesamiento y escritura.
    """
    # Define las rutas de los archivos de entrada y salida.
    # Asegúrate de que este archivo exista.
    employee_file_path = 'employees.csv'
    report_file_path = 'report.txt'

    # Ejecuta el proceso.
    employee_list = read_employees(employee_file_path)
    if employee_list:
        department_data = process_data(employee_list)
        write_report(department_data, report_file_path)
        print(f"Reporte generado exitosamente en '{report_file_path}'")


# Este bloque asegura que main() solo se ejecute cuando el script es llamado directamente.
if __name__ == "__main__":
    main()
