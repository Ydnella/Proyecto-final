import Funciones_de_tareas


def ordenar_por_prioridad(tareas):
    prioridad_orden = {'alta': 1, 'media': 2, 'baja': 3}
    tareas_ordenadas = sorted(
        tareas, key=lambda tarea: prioridad_orden.get(tarea[3].lower(), 4))
    return tareas_ordenadas


def imprimir_tareas(tareas):
    for tarea in tareas:
        print(
            f"Tarea: {tarea[1]}, Prioridad: {tarea[3]}, Estado: {tarea[5]}")


def imprimir_tareas_ordenadas_por_prioridad():
    tareas = Funciones_de_tareas.cargar_tareas()
    if not tareas:
        print("📌 No hay tareas registradas.")
        return

    tareas_ordenadas = ordenar_por_prioridad(tareas)
    imprimir_tareas(tareas_ordenadas)
