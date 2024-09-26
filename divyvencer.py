from datetime import datetime
import os
import sys
current_date = datetime.now().strftime('%d-%m-%Y')

def divyvencer():
    try:
        # Ruta del archivo a verificar
        #archivo_a_verificar = r'D:\RPA\AA\MP06. Pendientes\Inputs\24-08-2023\12pm\Archivo_Plano_EPS-12pm-24-08-2023.txt'
        archivo_a_verificar = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', f"Process\Archivo_Plano_EPS.txt")

        # Tamaño máximo en bytes (1GB)
        tamaño_maximo = 1024 * 1024 * 1024  # 1GB

        # Obtener el tamaño del archivo
        tamaño_archivo = os.path.getsize(archivo_a_verificar)

        # Verificar si el tamaño del archivo supera el tamaño máximo
        if tamaño_archivo > tamaño_maximo:
            print(f'El archivo {archivo_a_verificar} supera 1GB de tamaño ({tamaño_archivo} bytes).')
                
            # Directorio donde se guardarán los archivos divididos
            #directorio_salida = r'D:\RPA\AA\MP06. Pendientes\Outputs\30-08-2023\Process'
            directorio_salida = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', "Process")
            os.makedirs(directorio_salida, exist_ok=True)

            # Tamaño aproximado de cada archivo dividido en bytes (1GB)
            tamaño_objetivo = 1 * 1024 * 1024 * 1024  # 1GB

            # Variables para el encabezado y el segmento actual
            encabezado = None
            segmento_actual = []
            tamaño_actual = 0
            numero_segmento = 1

            # Abre el archivo original en modo lectura con codificación Latin-1
            with open(archivo_a_verificar, 'r', encoding='latin-1') as archivo:
                for linea in archivo:
                    # Si es la primera línea, guarda el encabezado
                    if encabezado is None:
                        encabezado = linea.strip()
                        continue
                    
                    # Agrega la línea actual al segmento
                    segmento_actual.append(linea)
                    tamaño_actual += len(linea)
                    
                    # Si el tamaño del segmento supera el objetivo, guarda el segmento en un archivo nuevo
                    if tamaño_actual >= tamaño_objetivo:
                        # Nombre del archivo dividido
                        nombre_archivo = os.path.join(directorio_salida, f'Parte_{numero_segmento}.txt')
                        
                        # Escribe el encabezado y los datos en el archivo dividido
                        with open(nombre_archivo, 'w', encoding='latin-1') as archivo_salida:
                            archivo_salida.write(encabezado + '\n')
                            archivo_salida.writelines(segmento_actual)
                        
                        # Reinicia el segmento actual y el tamaño
                        segmento_actual = []
                        tamaño_actual = 0
                        numero_segmento += 1

            # Si hay datos restantes en el último segmento, guárdalos en un archivo adicional
            if segmento_actual:
                nombre_archivo = os.path.join(directorio_salida, f'Parte_{numero_segmento}.txt')
                with open(nombre_archivo, 'w', encoding='latin-1') as archivo_salida:
                    archivo_salida.write(encabezado + '\n')
                    archivo_salida.writelines(segmento_actual)

            print(f'Archivos divididos guardados en {directorio_salida}')
            return 2
        else:
            print(f'El archivo {archivo_a_verificar} tiene un tamaño aceptable ({tamaño_archivo} bytes).')
            return 2

    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e)             

print(divyvencer())