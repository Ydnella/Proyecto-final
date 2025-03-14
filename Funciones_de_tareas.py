import random
import datetime


def generar_id():
    # Número aleatorio de 4 dígitos
    return str(random.randint(1000, 9999)for _ in range(4))


# tarea vacia
tareas = []


def cargar_tareas():
    try:
        with open(tarea, "r") as file:
            return [line.strip().split(" | ") for line in file.readlines()]
    except FileNotFoundError:
        return []

# Guarda la lista de tareas en el archivo TXT


def guardar_tareas(tareas):
    with open(tarea, "w") as file:
        for tarea in tareas:
            file.write(" | ".join(tarea) + "\n")


# funcion para crear una tarea
def crear_tarea():

    descripcion = input("Ingrese la descripcion de la tarea: ")
    fecha_limite = input("Ingrese la fecha limite (Dia/Mes/Año): ")
    prioridad = input("Ingrese la prioridad (alta, media, baja): ")
    categoria = input(
        "Ingrese la categoria (pendiente, en progreso, completada): ")

    # Crear identificador único para la tarea
    tareas_id = generar_id()
    while any(tarea["id"] == tareas_id for tarea in tareas):
        tareas_id = generar_id()  # Si el esta en uso pues crea otro

    # Crear tarea con los detalles que se ingresaron
    tarea = {
        "id": tareas_id,
        "descripcion": descripcion,
        "fecha_limite": fecha_limite,
        "prioridad": prioridad,
        "categoria": categoria,
        "estado": "Pendiente"
    }

    # agregar tarea a la lista y mostrar su id.
    tarea.append(tarea)
    print(f"Tarea creada con éxito. ID: {tareas_id}")


def leer_tareas():
    if not tareas:
        print("No hay tareas")
        return


# busca los datos en la lista y los imprime
print("Lista de tareas:")
for tarea in tareas:
    print(f"ID: {tarea['id']}, Descripción: {tarea['descripcion']}, Fecha Límite: {tarea['fecha_limite']}, Prioridad: {tarea['prioridad']}, Categoría: {tarea['categoria']}, Estado: {tarea['estado']}")


# funcion para actualizar la tarea

def actualizar_tarea():
    tareas = cargar_tareas()

    tarea_id = int(
        input("Ingrese el ID de la tarea que desea actualizar: "))  # Corregido

    # Buscar la tarea mediante el ID
    tarea_encontrada = None
    for tarea in tareas:
        if int(tarea[0]) == tarea_id:  # Convertimos ID de la tarea a int para comparar
            tarea_encontrada = tarea
            break

    if not tarea_encontrada:
        print("Tarea no encontrada.")
        return

    # pedir al usuario la informacion nueva
    descripcion = input(
        f"Nueva descripcion (actual: {tarea_encontrada[1]}): ") or tarea_encontrada[1]
    fecha_limite = input(
        f"Nueva fecha limite (actual: {tarea_encontrada[2]}): ") or tarea_encontrada[2]
    prioridad = input(
        f"Nueva prioridad (actual: {tarea_encontrada[3]}): ") or tarea_encontrada[3]
    categoria = input(
        f"Nueva categoria (actual: {tarea_encontrada[4]}): ") or tarea_encontrada[4]
    estado = input(
        f"Nuevo estado (pendiente, En progreso, Completada - actual: {tarea_encontrada[5]}): ") or tarea_encontrada[5]

    # Actualizar tarea con los nuevos valores
    tarea_encontrada[1] = descripcion
    tarea_encontrada[2] = fecha_limite
    tarea_encontrada[3] = prioridad
    tarea_encontrada[4] = categoria
    tarea_encontrada[5] = estado

    # Guardar cambios en el archivo
    guardar_tareas(tareas)
    print("Tarea actualizada con éxito.")


def recordar_tarea():
    tareas = cargar_tareas()
    dia_actual = datetime.date.today()  # obtiene la fecha actual

    for tarea in tareas:
        try:
            # Convertir limite fecha a objeto date
            fecha_tarea = datetime.datetime.strptime(
                tarea[2], "%d/%m/%Y").date()
            # calcula la fecha limite con la actual y si no esta completada mostrara el recordatorio
            if 0 <= (fecha_tarea - dia_actual).days <= 3 and tarea[5].lower() != "completada":
                # imprime el recordatorio
                print(
                    f"Recordatorio - ID: {tarea[0]}, Descripción: {tarea[1]}, Fecha Límite: {tarea[2]}")
        except ValueError:
            pass  # Ignorar fechas inválidas


def estadisticas():
    # cuanta los las tareas dependiendo su estado y los imprime
    tareas = cargar_tareas()
    total = len(tareas)
    completadas = sum(
        1 for tarea in tareas if tarea[5].lower() == "completada")
    pendientes = sum(1 for tarea in tareas if tarea[5].lower() == "pendiente")
    en_progreso = total - completadas - pendientes

    print(
        f"Total: {total}, Completadas: {completadas}, Pendientes: {pendientes}, En progreso: {en_progreso}")
