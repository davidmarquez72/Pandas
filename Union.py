import sys
import pandas as pd

def erroresCol():
    try:
        # Rutas de los archivos
        archivo_original = r"D:\MP74. Notificar Glosas Prestadores\04. Plantillas\COLSANITAS.txt"
        archivo_errores = r"D:\MP74. Notificar Glosas Prestadores\04. Plantillas\erroresCOLSANITAS.txt"

        # Listas para almacenar las líneas correctas y las líneas con errores
        lineas_correctas = []
        lineas_errores = []

        # Intenta leer el archivo CSV
        try:
            with open(archivo_original, 'r') as archivo:
                for linea in archivo:
                    campos = linea.split('|')
                    if len(campos) == 59:  # Ajusta el número de campos según tu estructura
                        lineas_correctas.append(linea)
                    else:
                        lineas_errores.append(linea)

            # Guarda las líneas con errores en un archivo aparte
            with open(archivo_errores, 'w') as archivo_errores:
                archivo_errores.writelines(lineas_errores)

            # Convierte las líneas correctas en un DataFrame
            frame = pd.DataFrame([line.split('|') for line in lineas_correctas])
            
        except Exception as e:
            print("Error al procesar el archivo:", str(e))

        return 2
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e)

def erroresMed():
    try:
        # Rutas de los archivos
        archivo_original = r"D:\MP74. Notificar Glosas Prestadores\04. Plantillas\MEDISANITAS.txt"
        archivo_errores = r"D:\MP74. Notificar Glosas Prestadores\04. Plantillas\erroresMEDISANITAS.txt"

        # Listas para almacenar las líneas correctas y las líneas con errores
        lineas_correctas = []
        lineas_errores = []

        # Intenta leer el archivo CSV
        try:
            with open(archivo_original, 'r') as archivo:
                for linea in archivo:
                    campos = linea.split('|')
                    if len(campos) == 59:  # Ajusta el número de campos según tu estructura
                        lineas_correctas.append(linea)
                    else:
                        lineas_errores.append(linea)

            # Guarda las líneas con errores en un archivo aparte
            with open(archivo_errores, 'w') as archivo_errores:
                archivo_errores.writelines(lineas_errores)

            # Convierte las líneas correctas en un DataFrame
            frame = pd.DataFrame([line.split('|') for line in lineas_correctas])
            
        except Exception as e:
            print("Error al procesar el archivo:", str(e))

        return 2
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e)

def union():
    try:
                
        #Leemos el archivo txt

        frame = pd.read_csv(r"D:\MP74. Notificar Glosas Prestadores\04. Plantillas\COLSANITAS.txt", sep = '|',low_memory=False,usecols=range(0, 59))
        frame2 = pd.read_csv(r"D:\MP74. Notificar Glosas Prestadores\04. Plantillas\MEDISANITAS.txt", sep = '|',low_memory=False,usecols=range(0, 59))
        frame_final = frame._append(frame2)

        #Convertimos a xlsx
        frame_final.to_excel(r'D:\MP74. Notificar Glosas Prestadores\04. Plantillas\Union.xlsx', index = None, sheet_name='Hoja1')
        return 2
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e)

print(erroresCol())
print(erroresMed())
print(union())
