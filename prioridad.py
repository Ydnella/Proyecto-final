# Description: Este archivo contiene la función ordenar_por_prioridad que recibe una lista de tareas y las ordena por prioridad.

def ordenar_por_prioridad(tareas):
    prioridad_orden = {'alta': 1, 'media': 2, 'baja': 3}
    tareas_ordenadas = sorted(
        tareas, key=lambda tarea: prioridad_orden[tarea['prioridad']])
    return tareas_ordenadas


def imprimir_tareas(tareas):
    for tarea in tareas:
        print(
            f"Tarea: {tarea['nombre']}, Prioridad: {tarea['prioridad']}, Estado: {tarea['estado']}")


# Ejemplo de uso
if __name__ == "__main__":
    tareas = [
        {'nombre': 'Tarea 1', 'prioridad': 'media', 'estado': 'pendiente'},
        {'nombre': 'Tarea 2', 'prioridad': 'alta', 'estado': 'completada'},
        {'nombre': 'Tarea 3', 'prioridad': 'baja', 'estado': 'en progreso'},
        {'nombre': 'Tarea 4', 'prioridad': 'alta', 'estado': 'pendiente'},
        {'nombre': 'Tarea 5', 'prioridad': 'media', 'estado': 'completada'}
    ]

    tareas_ordenadas = ordenar_por_prioridad(tareas)
    imprimir_tareas(tareas_ordenadas)
