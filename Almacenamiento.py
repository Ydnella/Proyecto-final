from  Funciones_de_tareas import imprimir_tareas
Archivo_tareas = "tareas.txt"


def cargar_tareas():
    tareas = []
    try:
        with open(Archivo_tareas, "r") as file:
            # leemos las tareas del archivo
            for line in file:
                # Elimina los espacios en blanco y divide los datos.
                datos_tarea = line.strip().split(" | ")
                if len(datos_tarea) == 6:  # Aseguramos que la tarea tenga 6 elementos
                    tareas.append(datos_tarea)
                else:
                    # Imprime la línea con datos incompletos.
                    print(f"Datos incompletos en la línea: {line.strip()}")
    except FileNotFoundError:
        print(f"Archivo {Archivo_tareas} no encontrado.")
        return []

    imprimir_tareas(tareas)
    return tareas

def guardar_tareas(tareas):
    with open(Archivo_tareas, "w") as file:  # Abre el archivo en modo escritura
        for tarea in tareas:
            # Escribe las tareas en el archivo
            file.write(" | ".join(tarea) + "\n")
    print(f"Tareas guardadas: {tareas}")

    imprimir_tareas(tareas)
