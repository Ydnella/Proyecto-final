import Funciones_de_tareas

def menu():
    print("1. Crear tarea")
    print("2. Leer tareas")
    print("3. Actualizar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")
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
                Funciones_de_tareas.crear_tarea()
                if input("¿Desea volver al menú principal? (s/n): ").lower() == 's':
                    break
        elif opcion == 2:
            while True:
                Funciones_de_tareas.leer_tareas()
                if input("¿Desea volver al menú principal? (s/n): ").lower() == 's':
                    break
        elif opcion == 3:
            while True:
                Funciones_de_tareas.actualizar_tarea()
                if input("¿Desea volver al menú principal? (s/n): ").lower() == 's':
                    break
        elif opcion == 4:
            while True:
                Funciones_de_tareas.eliminar_tarea()
                if input("¿Desea volver al menú principal? (s/n): ").lower() == 's':
                    break
        elif opcion == 5:
            break
        else:
            print("Opción no válida")
