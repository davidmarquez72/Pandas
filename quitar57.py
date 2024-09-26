import sys
import pandas as pd
import os
from datetime import datetime, timedelta
from openpyxl import load_workbook

def Quitar57():
    try:
        # fecha actual y sumar 1 dia
        current_date = datetime.now()
        current_date_hoy = datetime.now().strftime('%Y-%m-%d')
        sm1 = timedelta(1)
        current_date_1 = (current_date + sm1).strftime('%Y-%m-%d')

        # ruta citas
        ruta_citas = os.path.join(r'D:\MP68-Recordatorio de citas por Maria Maula\03.output',f'{current_date_hoy}',f'Citas Medicas Presenciales {current_date_1}.xlsx')

        # Leer el archivo Excel
        df = pd.read_excel(ruta_citas)

        # Quitar el '.0' al final de los números en la columna 'telefono1'
        df['Telefono 1'] = df['Telefono 1'].astype(str)
        df['Telefono 1'] = df['Telefono 1'].str.replace('.0', '')

        # Quitar el '.0' al final de los números en la columna 'telefono2'
        df['Telefono 2'] = df['Telefono 2'].astype(str)
        df['Telefono 2'] = df['Telefono 2'].str.replace('.0', '')

        # eliminar 57
        def eliminar_57(numero):
            numero_str = str(numero)
            if len(numero_str) >= 2 and numero_str[:2] == '57':
                return int(numero_str[2:])
            else:
                return numero

        df['Telefono 1'] = df['Telefono 1'].apply(eliminar_57)
        df['Telefono 2'] = df['Telefono 2'].apply(eliminar_57)

        # Guardar el archivo Excel 
        df.to_excel(ruta_citas, index=False)

        # Cargar el archivo de Excel
        wb = load_workbook(ruta_citas)

        # Obtener la hoja de trabajo actual
        hoja = wb["Sheet1"]

        # Renombrar la hoja de trabajo
        hoja.title = "Hoja1"
            
        # Guardar los cambios en el archivo
        wb.save(ruta_citas)
            
        # Cerrar el archivo
        wb.close()  
        return 2
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e)

