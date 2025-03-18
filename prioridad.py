# Description: Este archivo contiene la función ordernar_por_prioridad que recibe una lista de tareas y las ordena por prioridad.

def ordernar_por_prioridad(tareas):
    tareas.sort(key=lambda x: x[3])
    return tareas
