import sys
import pandas as pd
from datetime import datetime, timedelta
import os

def cruceCodigo():
    try:
        # fecha actual y sumar 1 dia
        current_date = datetime.now()
        current_date_hoy = datetime.now().strftime('%Y-%m-%d')
        sm1 = timedelta(1)
        current_date_1 = (current_date + sm1).strftime('%Y-%m-%d')

        # ruta citas
        ruta_citas = os.path.join(r'D:\MP68-Recordatorio de citas por Maria Maula\03.output',f'{current_date_hoy}',f'Citas Medicas Presenciales {current_date_1}.xlsx')

        # lee archivo de Codigos 
        dfcodigos = pd.read_excel(r"D:\MP68-Recordatorio de citas por Maria Maula\02.plantillas\Codigos.xlsx")


        # lee archivo citas medicas presenciales fecha
        dfcitas = pd.read_excel(ruta_citas)

        # Convertir la columna del segundo DataFrame al tipo de dato adecuado
        dfcodigos['Codigo del recurso'] = dfcodigos['Codigo del recurso'].astype(dfcitas['Codigo del recurso'].dtype)

        # cruce
        #cruce = pd.merge(dfcitas, dfcodigos, left_on='Codigo del recurso', right_on='Codigo del recurso', how='inner')
        cruce = pd.merge(dfcitas, dfcodigos, on='Codigo del recurso', how='inner')

        # Eliminar los registros encontrados en el cruce.xlsx
        # To check if values is not in the DataFrame, use the ~ operato
        reporte1_sin_cruce = dfcitas[~dfcitas['Codigo del recurso'].isin(dfcodigos['Codigo del recurso'])]

        # ruta guardar
        ruta_guardar = os.path.join(ruta_citas)
        ruta_guardar_cruce = os.path.join(r'D:\MP68-Recordatorio de citas por Maria Maula\03.output',f'{current_date_hoy}',f'Cruce_Codigos_{current_date_1}.xlsx')

        # Guardar resultado sin cruce
        reporte1_sin_cruce.to_excel(ruta_guardar, index=False)

        # Guardar los cruces en excel
        cruce.to_excel(ruta_guardar_cruce, index=False)
        return 2
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e)