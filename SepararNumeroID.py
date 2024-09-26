import sys
import pandas as pd
from datetime import datetime
import os

def separar():
    try:
        # fecha actual
        current_date = datetime.now().strftime('%Y-%m-%d')

        # ruta dinamica
        ruta_reporte = os.path.join('D:/MP74. Notificar Glosas Prestadores/03. Output', f'{current_date}/Reporte Glosas.xlsx')

        # Cargar el archivo Excel
        df = pd.read_excel(ruta_reporte)

        # Crear un diccionario de DataFrames separados por número de identificación
        dfs_dict = {}
        for identificacion in df['NÚMERO DE IDENTIFICACIÓN DEL PRESTADOR'].unique():
            dfs_dict[identificacion] = df[df['NÚMERO DE IDENTIFICACIÓN DEL PRESTADOR'] == identificacion]

        # Escribir cada DataFrame en un archivo Excel separado
        for identificacion, df in dfs_dict.items():
            nombre_archivo = f"D:/MP74. Notificar Glosas Prestadores/03. Output/{current_date}/{identificacion}.xlsx"
            df.to_excel(nombre_archivo, index=False)
        return 2
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e)    

