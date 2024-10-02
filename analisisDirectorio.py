import os # Rutas y archivos
import re # Regular expression
import sys 

# Verifica si se ha pasado un nombre de directorio y una extension como argumento

def directorio():
 if len(sys.argv) != 2:
    print("Uso: python analisisDirectorio.py <nombre_directorio>")
    sys.exit(1)
 nombre_directorio = sys.argv[1]

 if not os.path.exists(nombre_directorio): 
     print(f"El directorio {nombre_directorio} no existe.")
     sys.exit(1)
 return nombre_directorio 

def buscar_patron_en_archivos(directorio, patron, archivo_resultado):
    # Compilar el patron para hacer la busqueda mas eficiente
    regex = re.compile(patron)
    
    # Abrir archivo donde se guardan los resultados de la busqueda
    with open(archivo_resultado, 'w') as resultado:

        # Recorrer todos los archivos en el directorio
        for archivo in os.listdir(directorio):

            ruta_archivo = os.path.join(directorio, archivo)
            
            # Solo buscar en archivos de texto
            if os.path.isfile(ruta_archivo) and archivo.endswith('.txt'):
                with open(ruta_archivo, 'r', encoding='utf-8') as f:
                    lineas = f.readlines()
                    num_lineas = len(lineas)
                    num_palabras = 0
                    num_python = 0
                    for linea in lineas:
                     palabras = linea.split()
                     num_palabras += len(palabras) 
                     num_python += sum(1 for palabra in palabras if palabra.lower() == 'python')

                # Buscar el patron en cada linea
                for num_linea, linea in enumerate(lineas, 1):
                    if regex.search(linea):
                        # Escribir la linea coincidente en el archivo de resultados
                        resultado.write(f"Archivo: {archivo}\nLínea {num_linea}: {linea}\nNumero total de palabras: {num_palabras}\nNúmero de veces que aparece la palabra Python: {num_python}")

    print(f"Resultados guardados en {archivo_resultado}")

# Parametros para la busqueda
directorio_a_buscar = directorio()
# patron_a_buscar = r'patron'

patron_a_buscar = 'python'

archivo_salida = 'informe.txt'

# Llamada a la funcion para buscar el patron
buscar_patron_en_archivos(directorio_a_buscar, patron_a_buscar, archivo_salida)