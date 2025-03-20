import Funciones_de_tareas
import prioridad
import os
import sys
import time
import json
import Almacenamiento as al

current_time = time.localtime()
os.system('cls' if os.name == 'nt' else 'clear')
print("Cargando el sistema por favor espere...")
time.sleep(0.25)
os.system('cls' if os.name == 'nt' else 'clear')
print("Cargando el sistema por favor espere.")
time.sleep(0.25)
os.system('cls' if os.name == 'nt' else 'clear')
print("Cargando el sistema por favor espere..")
time.sleep(0.25)
os.system('cls' if os.name == 'nt' else 'clear')
print("Cargando el sistema por favor espere...")
time.sleep(0.25)
os.system('cls' if os.name == 'nt' else 'clear')
print("Cargando el sistema por favor espere.")
time.sleep(0.25)
os.system('cls' if os.name == 'nt' else 'clear')
print("Cargando el sistema por favor espere..")
time.sleep(0.25)
os.system('cls' if os.name == 'nt' else 'clear')
print("Esto puede tardar unos segundos...")
time.sleep(0.25)
os.system('cls' if os.name == 'nt' else 'clear')
print("Esto puede tardar unos segundos.")
time.sleep(0.25)
os.system('cls' if os.name == 'nt' else 'clear')
print("Esto puede tardar unos segundos..")
time.sleep(0.25)
os.system('cls' if os.name == 'nt' else 'clear')
print("Esto puede tardar unos segundos...")
time.sleep(0.25)
os.system('cls' if os.name == 'nt' else 'clear')
print("Esto puede tardar unos segundos.")
time.sleep(0.25)
os.system('cls' if os.name == 'nt' else 'clear')
print("Esto puede tardar unos segundos..")
time.sleep(0.25)
os.system('cls' if os.name == 'nt' else 'clear')
print("Esto puede tardar unos segundos...")
time.sleep(0.25)
os.system('cls' if os.name == 'nt' else 'clear')
print("Esto puede tardar unos segundos.")
time.sleep(0.25)
os.system('cls' if os.name == 'nt' else 'clear')
print("Esto puede tardar unos segundos..")
time.sleep(0.25)
os.system('cls' if os.name == 'nt' else 'clear')
print("Esto puede tardar unos segundos...")
time.sleep(0.25)
os.system('cls' if os.name == 'nt' else 'clear')
print("Esto puede tardar unos segundos.")
time.sleep(0.25)
os.system('cls' if os.name == 'nt' else 'clear')
print("Esto puede tardar unos segundos..")
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
print("ADVERTENCIA: este sistema es antiguo y puede tener errores")
print("por lo cual puede tardar en cargar")
print("por favor, no cierre el sistema mientras se carga")
time.sleep(4)
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(0.5)
os.system('cls' if os.name == 'nt' else 'clear')
print("Cargando datos de tareas.")
time.sleep(0.5)
os.system('cls' if os.name == 'nt' else 'clear')
print("Cargando datos de prioridades..")
time.sleep(0.5)
os.system('cls' if os.name == 'nt' else 'clear')
print("Cargando datos de archivos....")
time.sleep(0.5)
os.system('cls' if os.name == 'nt' else 'clear')
print("Cargando datos de estadísticas.")
time.sleep(0.5)
os.system('cls' if os.name == 'nt' else 'clear')
print("Cargando datos de ordenamiento..")
time.sleep(0.5)
os.system('cls' if os.name == 'nt' else 'clear')
print("Cargando datos de actualización...")
time.sleep(0.5)
os.system('cls' if os.name == 'nt' else 'clear')
print("Cargando datos de fecha y hora.")


def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Fecha y hora actual: ", time.strftime(
        "%d/%m/%Y %H:%M:%S", current_time))
    print("----------------------------------")
    print("Bienvenido al sistema de tareas")
    print("----------------------------------")
    print("Selecione una opción del menú:    ")
    print("Utlizando numeros del 1 al 7:")
    print("\n")
    print("         Menú principal          ")
    print("\n")
    print("         1. Crear tarea          ")
    print("         2. Leer tareas          ")
    print("         3. Actualizar tarea     ")
    print("         4. Eliminar tarea       ")
    print("         5. Estadísticas         ")
    print("         6. Ordenar por prioridad")
    print("\n")
    print("         7. Salir                ")
    print("----------------------------------")
    try:
        return int(input("Seleccione una opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return 0


if __name__ == "__main__":
    while True:
        opcion = menu()
        if opcion == 1:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Creando tarea...")
                time.sleep(0.25)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Creando tarea.")
                time.sleep(0.25)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Creando tarea..")
                time.sleep(0.25)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Creando tarea...")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Fecha y hora actual: ", time.strftime(
                    "%d/%m/%Y %H:%M:%S", current_time))
                print("----------------------------------")
                print("\n")
                print("         CREAR TAREA          ")
                print("\n")
                print("Haz elegido la opción de crear tarea")
                print("aqui podras crear una nueva tarea para tu lista")
                print("recuerda que puedes agregar una prioridad a tu tarea")
                print("\n")
                print("----------------------------------")
                print("\n")
                print("Por favor, ingrese los datos de la tarea:")
                print("\n")
                print("Formato de fecha: dd/mm/aaaa")
                print("\n")

                print("----------------------------------")
                Funciones_de_tareas.crear_tarea()
                print("----------------------------------")
                if input("Desea volver al menu principal? (s/n): ").lower() == 's':
                    break
        elif opcion == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Leyendo tareas...")
            time.sleep(0.25)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Leyendo tareas.")
            time.sleep(0.25)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Leyendo tareas..")
            time.sleep(0.25)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Leyendo tareas...")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Fecha y hora actual: ", time.strftime(
                "%d/%m/%Y %H:%M:%S", current_time))
            print("----------------------------------")
            print("\n")
            print("         LEER TAREAS          ")
            print("\n")
            print("Haz elegido la opción de leer tareas")
            print("aqui podras ver todas las tareas que tienes en tu lista")
            print("\n")
            print("----------------------------------")
            print("\n")
            print("Tareas:")
            while True:
                Funciones_de_tareas.leer_tareas()
                if input("Desea volver al menu principal? (s/n): ").lower() == 's':
                    break
        elif opcion == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Actualizando tarea...")
            time.sleep(0.25)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Actualizando tarea.")
            time.sleep(0.25)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Actualizando tarea..")
            time.sleep(0.25)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Actualizando tarea...")
            time.sleep(0.25)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Actualizando tarea.")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Fecha y hora actual: ", time.strftime(
                "%d/%m/%Y %H:%M:%S", current_time))
            print("----------------------------------")
            print("\n")
            print("         ACTUALIZAR TAREA          ")
            print("\n")
            print("Haz elegido la opción de actualizar tarea")
            print("aqui podras actualizar una tarea de tu lista")
            print("\n")
            print("----------------------------------")
            print("\n")
            print("Por favor, ingrese los datos de la tarea:")
            print("\n")
            print("Formato de fecha: dd/mm/aaaa")
            print("\n")
            time.sleep(4)
            os.system('cls' if os.name == 'nt' else 'clear')
            while True:
                Funciones_de_tareas.actualizar_tarea()
                if input("Desea volver al menu principal? (s/n): ").lower() == 's':
                    break
        elif opcion == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Eliminando tarea...")
            time.sleep(0.25)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Eliminando tarea.")
            time.sleep(0.25)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Eliminando tarea..")
            time.sleep(0.25)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Eliminando tarea...")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Fecha y hora actual: ", time.strftime(
                "%d/%m/%Y %H:%M:%S", current_time))
            print("----------------------------------")
            print("\n")
            print("         ELIMINAR TAREA          ")
            print("\n")
            print("Haz elegido la opción de eliminar tarea")
            print("aqui podras eliminar una tarea de tu lista")
            print("\n")
            print("----------------------------------")
            print("\n")
            print("Por favor, ingrese los datos de la tarea")
            print("que deseas eliminar:")
            print("\n")
            print("Formato de fecha: dd/mm/aaaa")
            print("\n")
            time.sleep(4)
            os.system('cls' if os.name == 'nt' else 'clear')
            while True:
                Funciones_de_tareas.eliminar_tarea()
                if input("Desea volver al menu principal? (s/n): ").lower() == 's':
                    break
        elif opcion == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Estadísticas...")
            time.sleep(0.25)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Estadísticas.")
            time.sleep(0.25)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Estadísticas..")
            time.sleep(0.25)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Estadísticas...")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Fecha y hora actual: ", time.strftime(
                "%d/%m/%Y %H:%M:%S", current_time))
            print("----------------------------------")
            print("\n")
            print("         ESTADÍSTICAS          ")
            print("\n")
            print("Haz elegido la opción de estadísticas")
            print("aqui podras ver las estadísticas de las tareas")
            print("que tienes en tu lista")
            print("\n")
            print("----------------------------------")
            print("\n")
            print("Estadísticas:")
            while True:
                Funciones_de_tareas.estadisticas()
                if input("Desea volver al menu principal? (s/n): ").lower() == 's':
                    break
        elif opcion == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            while True:
                print("Ordenando tareas...")
                time.sleep(0.25)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Ordenando tareas.")
                time.sleep(0.25)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Ordenando tareas..")
                time.sleep(0.25)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Ordenando tareas...")
                time.sleep(0.25)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Ordenando tareas.")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Fecha y hora actual: ", time.strftime(
                    "%d/%m/%Y %H:%M:%S", current_time))
                print("----------------------------------")
                print("\n")
                print("         ORDENAR POR PRIORIDAD          ")
                print("\n")
                print("Haz elegido la opción de ordenar por prioridad")
                print("aqui podras ver las tareas ordenadas por prioridad")
                print("\n")
                print("----------------------------------")
                print("\n")
                print("Tareas ordenadas por prioridad:")
                tareas_ordenadas = al.ordenar_por_prioridad()
                for tarea in tareas_ordenadas:
                    print(
                        f"Tarea: {tarea[1]}, Prioridad: {tarea[3]}, Estado: {tarea[5]}")
                if input("Desea volver al menu principal? (s/n): ").lower() == 's':
                    break
        elif opcion == 7:
            break
        else:
            print("Opción no válida")
            time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Saliendo del sistema...")
    time.sleep(0.25)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Saliendo del sistema.")
    time.sleep(0.25)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Saliendo del sistema..")
    time.sleep(0.25)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Saliendo del sistema...")
    time.sleep(0.25)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Saliendo del sistema.")
    time.sleep(0.25)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Saliendo del sistema..")
    time.sleep(0.25)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Saliendo del sistema...")
    time.sleep(0.25)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Saliendo del sistema.")
    time.sleep(0.25)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Saliendo del sistema..")
    time.sleep(0.25)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Saliendo del sistema...")
    time.sleep(0.25)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Gracias por usar el sistema de tareas.")
    print("Hasta luego.")
    sys.exit(0)
