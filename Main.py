import Funciones_de_tareas


def menu():
    print("1. Crear tarea")
    print("2. Leer tareas")  # Corregido
    print("3. Actualizar tarea")
    print("4. Salir")           # Corregido
    return int(input("Seleccione una opción: "))    # Corregido


if __name__ == "__main__":
    while True:
        opcion = menu()
        if opcion == 1:
            Funciones_de_tareas.crear_tarea()
        elif opcion == 2:
            Funciones_de_tareas.leer_tareas()
        elif opcion == 3:
            Funciones_de_tareas.actualizar_tarea()
        elif opcion == 4:
            break
        else:
            print("Opción no válida")
