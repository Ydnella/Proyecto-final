import random
import datetime

def generar_id():
    # Numero aleatorio de 4 dígitos
    return str(random.randint(1000, 9999))

Archivo_tareas = "tareas.txt"

def cargar_tareas():
    tareas = []
    try:
        with open(Archivo_tareas, "r") as file:
            # leemos las tareas del archivo
            for line in file:
                datos_tarea = line.strip().split(" | ")
                if len(datos_tarea) == 6:  # Aseguramos que la tarea tenga 6 elementos
                    tareas.append(datos_tarea)
                else:
                    print(f"Datos incompletos en la línea: {line.strip()}")
    except FileNotFoundError:
        print(f"Archivo {Archivo_tareas} no encontrado.")
        return []
    print(f"Tareas cargadas: {tareas}")
    return tareas

def guardar_tareas(tareas):
    with open(Archivo_tareas, "w") as file:
        for tarea in tareas:
            file.write(" | ".join(tarea) + "\n")
    print(f"Tareas guardadas: {tareas}")

def crear_tarea():
    descripcion = input("Ingrese la descripcion de la tarea: ")
    fecha_limite = input("Ingrese la fecha limite (Dia/Mes/Año): ")
    prioridad = input("Ingrese la prioridad (alta, media, baja): ")
    categoria = input("Ingrese la categoria: ")
    estado = str (input("Ingrese el estado de la tarea (pendiente, en progreso, completada): "))

    # Crear identificador único para la tarea
    tareas_id = generar_id()
    tareas = cargar_tareas()  # Cargar tareas para asegurar que el ID sea único
    while any(tarea[0] == tareas_id for tarea in tareas):
        tareas_id = generar_id()  # Si el id está en uso, genera otro

    # Crear tarea con los detalles que se ingresaron
    tarea = [tareas_id, descripcion, fecha_limite, prioridad, categoria, estado]

    # Cargar tareas y agregar la nueva tarea
    tareas.append(tarea)
    guardar_tareas(tareas)  # Guardar las tareas actualizadas
    print(f"Tarea creada con éxito. ID: {tareas_id}")

def leer_tareas():
    tareas = cargar_tareas()

    if not tareas:
        print("📌 No hay tareas registradas.")
        return

    print("\n📋 Lista de tareas:")
    for tarea in tareas:
        if len(tarea) == 6:  # Aseguramos que la tarea tenga 6 elementos
            print(f"🆔 ID: {tarea[0]}")
            print(f"📝 Descripción: {tarea[1]}")
            print(f"📅 Fecha Límite: {tarea[2]}")
            print(f"⚡ Prioridad: {tarea[3]}")
            print(f"📂 Categoría: {tarea[4]}")
            print(f"✅ Estado: {tarea[5]}")
            print("-" * 40)
        else:
            print(f"Tarea con ID {tarea[0]} tiene datos incompletos.")

def actualizar_tarea():
    tareas = cargar_tareas()

    tarea_id = input("Ingrese el ID de la tarea que desea actualizar: ")

    # Buscar la tarea mediante el ID
    tarea_encontrada = None
    for tarea in tareas:
        if tarea[0] == tarea_id:
            tarea_encontrada = tarea
            break

    if not tarea_encontrada:
        print("Tarea no encontrada.")
        return

    # Pedir al usuario la información nueva
    descripcion = input(f"Nueva descripcion (actual: {tarea_encontrada[1]}): ") or tarea_encontrada[1]
    fecha_limite = input(f"Nueva fecha limite (actual: {tarea_encontrada[2]}): ") or tarea_encontrada[2]
    prioridad = input(f"Nueva prioridad (actual: {tarea_encontrada[3]}): ") or tarea_encontrada[3]
    categoria = input(f"Nueva categoria (actual: {tarea_encontrada[4]}): ") or tarea_encontrada[4]
    estado = input(f"Nuevo estado (pendiente, en progreso, completada - actual: {tarea_encontrada[5]}): ") or tarea_encontrada[5]

    # Actualizar tarea con los nuevos valores
    tarea_encontrada[1] = descripcion
    tarea_encontrada[2] = fecha_limite
    tarea_encontrada[3] = prioridad
    tarea_encontrada[4] = categoria
    tarea_encontrada[5] = estado

    # Guardar cambios en el archivo
    guardar_tareas(tareas)
    print("Tarea actualizada con éxito.")

def eliminar_tarea():
    tareas = cargar_tareas()

    tarea_id = input("Ingrese el ID de la tarea que desea eliminar: ")

    # Buscar la tarea mediante el ID
    tarea_encontrada = None
    for tarea in tareas:
        if tarea[0] == tarea_id:
            tarea_encontrada = tarea
            break

    if not tarea_encontrada:
        print("Tarea no encontrada.")
        return

    # Eliminar la tarea
    tareas.remove(tarea_encontrada)

    # Guardar cambios en el archivo
    guardar_tareas(tareas)
    print("Tarea eliminada con éxito.")

def recordar_tarea():
    tareas = cargar_tareas()
    dia_actual = datetime.date.today()  # Obtiene la fecha actual

    for tarea in tareas:
        try:
            # Convertir límite de fecha a objeto date
            fecha_tarea = datetime.datetime.strptime(tarea[2], "%d/%m/%Y").date()
            # Calcula la fecha límite con la actual y si no está completada, muestra el recordatorio
            if 0 <= (fecha_tarea - dia_actual).days <= 3 and tarea[5].lower() != "completada":
                # Imprime el recordatorio
                print(f"Recordatorio - ID: {tarea[0]}, Descripción: {tarea[1]}, Fecha Límite: {tarea[2]}")
        except ValueError:
            pass  # Ignorar fechas inválidas

def estadisticas():
    tareas = cargar_tareas()
    total = len(tareas)
    completadas = sum(1 for tarea in tareas if tarea[5].lower() == "completada")
    pendientes = sum(1 for tarea in tareas if tarea[5].lower() == "pendiente")
    en_progreso = total - completadas - pendientes

    print(f"Total: {total}, Completadas: {completadas}, Pendientes: {pendientes}, En progreso: {en_progreso}")



