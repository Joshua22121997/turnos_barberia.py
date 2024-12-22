Este proyecto Python es una aplicación de línea de comandos diseñada para gestionar los turnos de una barbería. Permite agregar, mostrar y eliminar turnos de manera organizada, facilitando la gestión de la agenda.
Funcionalidades principales:
    • Agregar turnos: Permite ingresar el nombre del cliente, la fecha y la hora del turno. Valida la entrada para asegurar que la fecha y hora sean correctas.
    • Mostrar turnos: Presenta una lista ordenada de todos los turnos registrados, mostrando el nombre del cliente y la fecha y hora del turno.
    • Eliminar turnos: Permite eliminar un turno específico de la lista, solicitando al usuario el número del turno a eliminar.
Cómo usar:
    1. Ejecutar el programa: Ejecuta el archivo Python desde tu terminal o línea de comandos.
    2. Seleccionar opciones: El programa mostrará un menú con las siguientes opciones:
        -Agregar Turno
        -Mostrar Turnos
        -Eliminar Turno
        -Salir
    3. Interactuar: Sigue las instrucciones en pantalla para realizar las acciones deseadas. 
    Estructura del código:
    • turnos: Una lista que almacena los datos de cada turno en forma de diccionarios.
    • Funciones:
        1.agregar_turno(): Agrega un nuevo turno a la lista.
        2.mostrar_turnos(): Muestra la lista de turnos ordenados por fecha y hora.
        3.eliminar_turno(): Elimina un turno específico de la lista.
        4.menu(): Presenta el menú principal y maneja las opciones del usuario.
   
