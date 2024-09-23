import sys
import pandas as pd
from datetime import datetime
import os

def Centros():
    try:
        # fecha actual y sumar 1 dia
        current_date = datetime.now().strftime('%Y-%m-%d')

        # lee archivo de PRESTADORES CENTROS MEDICOS_GLOSAS
        df_centros_medicos = pd.read_excel(r"D:\MP74. Notificar Glosas Prestadores\02. Inputs\PRESTADORES CENTROS MEDICOS_GLOSAS.xlsx")

        # ruta de archivo de reporte glosas
        ruta_reporte = os.path.join('D:/MP74. Notificar Glosas Prestadores/03. Output', f'{current_date}/Reporte Glosas.xlsx')

        # lee archivo REPORTE_DE_GLOSAS_BH_2
        df_reporte = pd.read_excel(ruta_reporte)

        # cruce
        cruce = pd.merge(df_centros_medicos, df_reporte, left_on='ID MEDICO', right_on='NÚMERO DE IDENTIFICACIÓN DEL PRESTADOR', how='inner')

        #ruta cruce
        ruta_guardar_cruce = os.path.join(r"D:\MP74. Notificar Glosas Prestadores\03. Output",f'{current_date}',f'Reporte de Glosas Prestadores Centros Médicos {current_date}.xlsx')

        # Guardar los cruces en excel
        if cruce.empty:
            print("nothing")
        else:
            cruce.to_excel(ruta_guardar_cruce, index=False)
        
        return 2
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e)   