import Funciones_de_tareas
import prioridad


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
    print("         4. Eliminar tarea       ")
    print("         5. Estadísticas         ")
    print("         6. Ordenar por prioridad")
    print("\n")
    print("         7. Salir                ")
    print("\n")
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
                Funciones_de_tareas.actualizar_tarea()
                if input("Desea volver al menu principal? (s/n): ").lower() == 's':
                    break
        elif opcion == 4:
            while True:
                Funciones_de_tareas.eliminar_tarea()
                if input("Desea volver al menu principal? (s/n): ").lower() == 's':
                    break
        elif opcion == 5:
            while True:
                Funciones_de_tareas.estadisticas()
                if input("Desea volver al menu principal? (s/n): ").lower() == 's':
                    break
        elif opcion == 6:
            while True:
                tareas = Funciones_de_tareas.leer_tareas()
                tareas_ordenadas = prioridad.ordenar_por_prioridad(tareas)
                prioridad.imprimir_tareas(tareas_ordenadas)
                if input("Desea volver al menu principal? (s/n): ").lower() == 's':
                    break
        elif opcion == 7:
            break
        else:
            print("Opción no válida")
