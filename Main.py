import Funciones_de_tareas

def menu():
    print("----------------------------------")
    print("\n")
    print("Bienvenido al sistema de tareas")
    print("\n")
    print("         Menú principal          ")
    print("\n")
    print("         1. Crear tarea          ")
    print("         2. Leer tareas          ")
    print("         3. Actualizar tarea     ")
    print("         4. Cargar tareas        ")
    print("\n")
    print("         5. Salir")
    print("\n")
    print("----------------------------------")
    return int(input("Seleccione una opción: "))


if __name__ == "__main__":
    while True:
        opcion = menu()
        if opcion == 1:
            while True:
                Funciones_de_tareas.crear_tarea()
                if input("Desea volver al menu principal? (s/n): ").lower() == 's':
                    break
        elif opcion == 2:
            while True:
                Funciones_de_tareas.leer_tareas()
                if input("Desea volver al menu principal? (s/n): ").lower() == 's':
                    break
        elif opcion == 3:
            while True:
                Funciones_de_tareas.cargar_tareas()
                if input("Desea volver al menu principal? (s/n): ").lower() == 's':
                    break
        elif opcion == 4:
            while True:
                Funciones_de_tareas.actualizar_tarea()
                if input("Desea volver al menu principal? (s/n): ").lower() == 's':
                    break
        elif opcion == 5:
            break
        else:
            print("Opción no válida")
