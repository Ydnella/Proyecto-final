def cargar_tareas():
    Archivo_tareas = "tareas.txt"
    tareas = []
    try:
        with open(Archivo_tareas, "r") as file:
            for line in file:
                datos_tarea = line.strip().split(" | ")
                if len(datos_tarea) == 6:
                    tareas.append(datos_tarea)
                else:
                    print(f"Datos incompletos en la línea: {line.strip()}")
    except FileNotFoundError:
        print(f"Archivo {Archivo_tareas} no encontrado.")
        return []
    return tareas


def ordenar_por_prioridad(tareas):
    prioridad_orden = {'alta': 1, 'media': 2, 'baja': 3}
    tareas_ordenadas = sorted(
        tareas, key=lambda tarea: prioridad_orden.get(tarea[3].lower(), 4))
    return tareas_ordenadas


def imprimir_tareas(tareas):
    for tarea in tareas:
        print(f"ID: {tarea[0]}")
        print(
            f"Descripción: {tarea[1]}, Fecha límite: {tarea[2]}, Prioridad: {tarea[3]}, Categoría: {tarea[4]}, Estado: {tarea[5]}")
        print("-" * 40)
