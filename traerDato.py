import sys
from openpyxl import load_workbook
from datetime import datetime
import os

# fecha actual
current_date = datetime.now().strftime('%d-%m-%Y')

# ruta dinamica
ruta = os.path.join('D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', f'Informe_Ejecucion_{current_date}.xlsx')

def traerDato():
    try:
        
        # fecha actual
        current_date = datetime.now().strftime('%d-%m-%Y')

        # ruta dinamica
        ruta = os.path.join('D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', f'Informe_Ejecucion_{current_date}.xlsx')

        wb = load_workbook(ruta)
        hoja = wb["Procesamiento Primera Ejecucion"]
        # --------------------- 12:00 ---------------------
        Planos12 = hoja["B2"].value
        PlanosEPS12 = hoja["B3"].value
        PendientesMP12 = hoja["B4"].value
        PendientesEPS12 = hoja["B5"].value
        # --------------------- 10:00 ---------------------
        Planos10 = hoja["B6"].value
        PlanosEPS10 = hoja["B7"].value
        PendientesMP10 = hoja["B8"].value
        PendientesEPS10 = hoja["B9"].value   
        # --------------------- 1:00 ---------------------
        Planos1 = hoja["B10"].value
        PlanosEPS1 = hoja["B11"].value
        PendientesMP1 = hoja["B12"].value
        PendientesEPS1 = hoja["B13"].value   
        # --------------------- 4:00 ---------------------
        Planos4 = hoja["B14"].value
        PlanosEPS4 = hoja["B15"].value
        PendientesMP4 = hoja["B16"].value
        PendientesEPS4 = hoja["B17"].value   

        resultado = str(Planos12) + "," + str(PlanosEPS12) + "," + str(PendientesMP12) + "," + str(PendientesEPS12) + "," + \
        str(Planos10) + "," + str(PlanosEPS10) + "," + str(PendientesMP10) + "," + str(PendientesEPS10) + "," + \
        str(Planos1)  + "," + str(PlanosEPS1)  + "," + str(PendientesMP1)  + "," + str(PendientesEPS1) + "," + \
        str(Planos4)  + "," + str(PlanosEPS4)  + "," + str(PendientesMP4)  + "," + str(PendientesEPS4) 
        return resultado
    except Exception as e: 
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e)


