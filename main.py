from empleado import Empleado, Jefe
from area import Area

def guardar_datos(empleados, jefes, areas):
    """Guarda los datos en sus respectivos archivos."""
    with open("empleados.txt", "w") as f_emp, open("jefes.txt", "w") as f_jef, open("areas.txt", "w") as f_area:
        for empleado in empleados:
            empleado.guardar_en_archivo(f_emp)
        for jefe in jefes:
            jefe.guardar_en_archivo(f_jef)
        for area in areas:
            area.guardar_en_archivo(f_area)

def cargar_datos():
    """Carga los datos desde los archivos y elimina duplicados."""
    empleados = Empleado.cargar_desde_archivo("empleados.txt")
    jefes = Jefe.cargar_desde_archivo("jefes.txt", empleados)
    areas = Area.cargar_desde_archivo("areas.txt", empleados)
    return empleados, jefes, areas

def agregar_empleado(empleados):
    """Agrega un nuevo empleado desde datos ingresados por el usuario."""
    print("\n--- Agregar Empleado ---")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    salario = float(input("Salario: "))
    dni = input("DNI: ")
    fecha_vinculacion = input("Fecha de Vinculación (YYYY-MM-DD): ")
    nuevo_empleado = Empleado(nombre, apellido, edad, salario, dni, fecha_vinculacion)
    empleados.append(nuevo_empleado)
    print(f"Empleado agregado: {nuevo_empleado}")
    return nuevo_empleado

def gestionar_empleados(empleados):
    """Submenú para gestionar empleados."""
    menu_empleados = [
        "\n--- Gestión de Empleados ---",
        "1. Agregar Empleado",
        "2. Eliminar Empleado",
        "3. Modificar Empleado",
        "4. Mostrar Empleados",
        "5. Volver al Menú Principal"
    ]

    while True:
        for opcion in menu_empleados:
            print(opcion)
        seleccion = input("Seleccione una opción: ")

        if seleccion == "1":
            agregar_empleado(empleados)
        elif seleccion == "2":
            dni = input("Ingrese el DNI del empleado a eliminar: ")
            Empleado.eliminar_empleado(empleados, dni)
        elif seleccion == "3":
            dni = input("Ingrese el DNI del empleado a modificar: ")
            nuevo_nombre = input("Nuevo nombre (dejar vacío para no modificar): ") or None
            nuevo_apellido = input("Nuevo apellido (dejar vacío para no modificar): ") or None
            nueva_edad = input("Nueva edad (dejar vacío para no modificar): ")
            nueva_edad = int(nueva_edad) if nueva_edad else None
            nuevo_salario = input("Nuevo salario (dejar vacío para no modificar): ")
            nuevo_salario = float(nuevo_salario) if nuevo_salario else None
            Empleado.modificar_empleado(empleados, dni, nuevo_nombre, nuevo_apellido, nueva_edad, nuevo_salario)
        elif seleccion == "4":
            print("\nEmpleados registrados:")
            for empleado in empleados:
                print(empleado)
        elif seleccion == "5":
            break
        else:
            print("Opción no válida, intente de nuevo.")

def mostrar_menu_principal():
    """Despliega el menú principal y gestiona las opciones."""
    menu = [
        "\n--- Menú Principal ---",
        "1. Gestionar Empleados",
        "2. Gestionar Jefes",
        "3. Gestionar Áreas",
        "4. Salir"
    ]

    while True:
        for opcion in menu:
            print(opcion)
        seleccion = input("Seleccione una opción: ")

        if seleccion == "1":
            gestionar_empleados(empleados)
        elif seleccion == "2":
            print("Gestión de Jefes - Pendiente de implementación.")
        elif seleccion == "3":
            print("Gestión de Áreas - Pendiente de implementación.")
        elif seleccion == "4":
            print("Saliendo del programa. ¡Hasta pronto!")
            guardar_datos(empleados, jefes, areas)
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    # Cargar datos desde los archivos
    empleados, jefes, areas = cargar_datos()

    # Crear datos de prueba si los archivos están vacíos
    if not empleados and not jefes and not areas:
        empleado1 = Empleado("Ana", "Perez", 30, 50000, "12345678", "2022-01-15")
        jefe1 = Jefe("Carlos", "Lopez", 40, 80000, "87654321", "2020-05-20")
        jefe1.agregar_empleado(empleado1)
        area1 = Area("Desarrollo", "Encargada del desarrollo de software.")
        area1.agregar_empleado(empleado1)

        empleados.append(empleado1)
        jefes.append(jefe1)
        areas.append(area1)

        guardar_datos(empleados, jefes, areas)

    # Mostrar el menú principal
    mostrar_menu_principal()                                                       