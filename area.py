class Area:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.empleados = []
        

    def agregar_empleado(self, empleado):
        if empleado not in self.empleados:
            self.empleados.append(empleado)

    def mostrar_empleados(self):
        print(f"Empleados en el área {self.nombre}:")
        for emp in self.empleados:
            print(f" - {emp.nombre} {emp.apellido}")

    def guardar_en_archivo(self, archivo):
        archivo.write(f"{self.nombre},{self.descripcion}\n")
        for emp in self.empleados:
            archivo.write(f"Empleado:{emp.dni}\n")

    @staticmethod
    def eliminar_area(lista_areas, nombre_area):
        for area in lista_areas:
            if area.nombre == nombre_area:
                lista_areas.remove(area)
                print(f"Área '{nombre_area}' eliminada correctamente.")
                return
        print(f"No se encontró el área '{nombre_area}'.")

    @staticmethod
    def modificar_area(lista_areas, nombre_area, nuevo_nombre=None, nueva_descripcion=None):
        for area in lista_areas:
            if area.nombre == nombre_area:
                if nuevo_nombre:
                    area.nombre = nuevo_nombre
                if nueva_descripcion:
                    area.descripcion = nueva_descripcion
                print(f"Área '{nombre_area}' modificada correctamente.")
                return
        print(f"No se encontró el área '{nombre_area}'.")

    @staticmethod
    def cargar_desde_archivo(nombre_archivo, empleados):
        areas = []
        try:
            with open(nombre_archivo, "r") as f:
                area_actual = None
                for linea in f:
                    datos = linea.strip().split(",")
                    if len(datos) == 2:  # Área
                        nombre, descripcion = datos
                        area_actual = Area(nombre, descripcion)
                        areas.append(area_actual)
                    elif "Empleado:" in linea and area_actual:
                        dni = linea.split(":")[1].strip()
                        empleado = next((e for e in empleados if e.dni == dni), None)
                        if empleado:
                            area_actual.agregar_empleado(empleado)
        except FileNotFoundError:
            pass
        return areas
