import sys
import pandas as pd
#import unidecode
from unidecode import unidecode
import os
from datetime import datetime
from openpyxl import load_workbook

def QuitarCaracteres():
    try:
        # fecha actual
        current_date = datetime.now().strftime('%Y-%m-%d')

        # ruta dinamica
        ruta_base = os.path.join(r'D:\MP68-Recordatorio de citas por Maria Maula\03.output', f'{current_date}', "base.xlsx")

        # Leer el archivo Excel
        df = pd.read_excel(ruta_base)

        # Aplicar la función unidecode para eliminar las tildes
        df = df.applymap(lambda x: unidecode(str(x)))

        # Remover las comillas dobles y sencillas
        df = df.replace({'\'': '', '\"': ''}, regex=True)

         # Quitar el '.0' al final de los números en la columna 'telefono1'
        df['Telefono 1'] = df['Telefono 1'].astype(str)
        df['Telefono 1'] = df['Telefono 1'].str.replace('.0', '')

        # Quitar el '.0' al final de los números en la columna 'telefono2'
        df['Telefono 2'] = df['Telefono 2'].astype(str)
        df['Telefono 2'] = df['Telefono 2'].str.replace('.0', '')
        
        #  Quitar el '.0' al final de los números en la columna 'Codigo de la sede'
        df['Codigo de la sede'] = df['Codigo de la sede'].astype(str)
        df['Codigo de la sede'] = df['Codigo de la sede'].str.replace('.0', '')

        # Quitar el '.0' al final de los números en la columna 'Numero de documento del paciente'
        df['Numero de documento del paciente'] = df['Numero de documento del paciente'].astype(str)
        df['Numero de documento del paciente'] = df['Numero de documento del paciente'].str.replace('.0', '')



        # Guardar el archivo Excel sin las tildes y comillas
        df.to_excel(ruta_base, index=False)

        # Cargar el archivo de Excel
        wb = load_workbook(ruta_base)
        
        # Obtener la hoja de trabajo actual
        hoja = wb["Sheet1"]

        # Renombrar la hoja de trabajo
        hoja.title = "Hoja1"
            
        # Guardar los cambios en el archivo
        wb.save(ruta_base)
            
        # Cerrar el archivo
        wb.close()
        return 2
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e)

print(QuitarCaracteres())