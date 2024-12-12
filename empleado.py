class Empleado:
    def __init__(self, nombre, apellido, edad, salario, dni, fecha_vinculacion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.salario = float(salario)
        self.dni = dni
        self.fecha_vinculacion = fecha_vinculacion

    def __str__(self):
        return (f"Empleado: {self.nombre} {self.apellido}, Edad: {self.edad}, "
                f"Salario: {self.salario}, DNI: {self.dni}, "
                f"Fecha de Vinculación: {self.fecha_vinculacion}")

    def guardar_en_archivo(self, archivo):
        archivo.write(f"{self.nombre},{self.apellido},{self.edad},{self.salario},{self.dni},{self.fecha_vinculacion}\n")

    @staticmethod
    def eliminar_empleado(lista_empleados, dni):
        for empleado in lista_empleados:
            if empleado.dni == dni:
                lista_empleados.remove(empleado)
                print(f"Empleado con DNI {dni} eliminado correctamente.")
                return
        print(f"No se encontró un empleado con el DNI {dni}.")

    @staticmethod
    def modificar_empleado(lista_empleados, dni, nuevo_nombre=None, nuevo_apellido=None, nueva_edad=None, nuevo_salario=None):
        for empleado in lista_empleados:
            if empleado.dni == dni:
                if nuevo_nombre:
                    empleado.nombre = nuevo_nombre
                if nuevo_apellido:
                    empleado.apellido = nuevo_apellido
                if nueva_edad:
                    empleado.edad = nueva_edad
                if nuevo_salario:
                    empleado.salario = nuevo_salario
                print(f"Empleado con DNI {dni} modificado correctamente.")
                return
        print(f"No se encontró un empleado con el DNI {dni}.")

    @staticmethod
    def cargar_desde_archivo(nombre_archivo):
        empleados = []
        try:
            with open(nombre_archivo, "r") as f:
                for linea in f:
                    datos = linea.strip().split(",")
                    if len(datos) == 6:
                        empleados.append(Empleado(*datos))
        except FileNotFoundError:
            pass
        return empleados




class Jefe(Empleado):
    def __init__(self, nombre, apellido, edad, salario, dni, fecha_vinculacion):
        super().__init__(nombre, apellido, edad, salario, dni, fecha_vinculacion)
        self.empleados_a_cargo = []

    def agregar_empleado(self, empleado):
        if empleado not in self.empleados_a_cargo:
            self.empleados_a_cargo.append(empleado)

    def guardar_en_archivo(self, archivo):
        super().guardar_en_archivo(archivo)
        for emp in self.empleados_a_cargo:
            archivo.write(f"Empleado A Cargo:{emp.dni}\n")

    @staticmethod
    def eliminar_jefe(lista_jefes, dni):
        for jefe in lista_jefes:
            if jefe.dni == dni:
                lista_jefes.remove(jefe)
                print(f"Jefe con DNI {dni} eliminado correctamente.")
                return
        print(f"No se encontró un jefe con el DNI {dni}.")

    @staticmethod
    def modificar_jefe(lista_jefes, dni, nuevo_nombre=None, nuevo_apellido=None, nueva_edad=None, nuevo_salario=None):
        for jefe in lista_jefes:
            if jefe.dni == dni:
                if nuevo_nombre:
                    jefe.nombre = nuevo_nombre
                if nuevo_apellido:
                    jefe.apellido = nuevo_apellido
                if nueva_edad:
                    jefe.edad = nueva_edad
                if nuevo_salario:
                    jefe.salario = nuevo_salario
                print(f"Jefe con DNI {dni} modificado correctamente.")
                return
        print(f"No se encontró un jefe con el DNI {dni}.")

    @staticmethod
    def cargar_desde_archivo(nombre_archivo, empleados):
        jefes = []
        try:
            with open(nombre_archivo, "r") as f:
                for linea in f:
                    datos = linea.strip().split(",")
                    if len(datos) == 6:
                        jefe = Jefe(*datos)
                        jefes.append(jefe)
        except FileNotFoundError:
            pass
        return jefes
