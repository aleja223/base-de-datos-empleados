# def formatear_archivo(archivo):
#     with open(archivo, 'r', encoding='utf-8') as f:
#         contenido = f.read()
    
#     # Insertar un salto de línea antes de cada empleado que comienza con un nombre seguido de una coma
#     contenido_corregido = contenido.replace("2022-01-15Luis,", "2022-01-15\nLuis,")

#     with open(archivo, 'w', encoding='utf-8') as f:
#         f.write(contenido_corregido)

# # Llamar a la función
# formatear_archivo("empleados.txt")
