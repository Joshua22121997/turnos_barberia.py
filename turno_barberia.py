import datetime
turnos = []
def agregar_turno():
    nombre = input("Ingresa el nombre del cliente: ")
    fecha = input("Ingresa la fecha del turno (formato YYYY-MM-DD) : ")
    hora = input("Ingresa la hora del turno (formato HH:MM) : ")
    try :
        fecha_hora = datetime.datetime.strptime(f"{fecha} {hora}", "%Y-%m-%d %H:%M")
        turnos.append({"nombre": nombre, "fecha_hora": fecha_hora})
        print(f"Turno agregado para {nombre} el {fecha_hora.strftime('%Y-%m-%d %H:%M')}")
    except ValueError:
        print("Fecha u hora no válidas. Inténtalo nuevamente.")
def mostrar_turnos():
    if not turnos:
        print("No hay turnos registrados.")
        return

    print("\nLista de turnos:")
    for i, turno in enumerate(sorted(turnos, key=lambda x: x['fecha_hora']), start=1):
        print(f"{i}. {turno['nombre']} - {turno['fecha_hora'].strftime('%Y-%m-%d %H:%M')}")
    print()
def eliminar_turno():
    mostrar_turnos()
    if not turnos:
        return

    try:
        indice = int(input("Ingresa el número del turno a eliminar: ")) - 1
        if 0 <= indice < len(turnos):
            eliminado = turnos.pop(indice)
            print(f"Turno de {eliminado['nombre']} eliminado.")
        else:
            print("Número de turno no válido.")
    except ValueError:
        print("Entrada inválida. Intenta nuevamente.")

def menu():
    while True:
        print("\n--- Sistema de Turnos para Barbería ---")
        print("1. Agregar Turno")
        print("2. Mostrar Turnos")
        print("3. Eliminar Turno")
        print("4. Salir")

        opcion = input("Elige una opción: ")
        if opcion == "1":
            agregar_turno()
        elif opcion == "2":
            mostrar_turnos()
        elif opcion == "3":
            eliminar_turno()
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    menu()

