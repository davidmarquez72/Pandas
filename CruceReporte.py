import sys
import pandas as pd
from datetime import datetime
import os

def noReporte():
    try:
                
        # fecha actual
        current_date = datetime.now().strftime('%d%m%Y')

        # ruta dinamica
        ruta_reporte = os.path.join(r'D:\MP74. Notificar Glosas Prestadores\02. Inputs', f'No reportar {current_date}.xlsx')

        # lee archivo de archivo generado
        dfrepgen = pd.read_excel(r"D:\MP74. Notificar Glosas Prestadores\04. Plantillas\REPORTE_DE_GLOSAS_BH.xlsx")

        # valida si exite el archivo 
        if os.path.exists(ruta_reporte):
            # lee archivo de input "No reportar DDMMYYYY.xlsx"
            #dfrepinput = pd.read_excel(r"D:\MP74. Notificar Glosas Prestadores\02. Inputs\No reportar 17042023.xlsx")
            dfrepinput = pd.read_excel(ruta_reporte)

            # cruce
            cruce = pd.merge(dfrepgen, dfrepinput, on='ID GLOSA', how='inner')

            # Eliminar los registros encontrados en el reporte1
            reporte1_sin_cruce = dfrepgen[~dfrepgen['ID GLOSA'].isin(cruce['ID GLOSA'])]

            # Guardar los resultados en dos archivos Excel diferentes
            cruce.to_excel(r"D:\MP74. Notificar Glosas Prestadores\04. Plantillas\cruce.xlsx", index=False)
            reporte1_sin_cruce.to_excel(r"D:\MP74. Notificar Glosas Prestadores\04. Plantillas\REPORTE_DE_GLOSAS_BH_1.xlsx", index=False)
            print("El archivo existe.")
        else:
            dfrepgen.to_excel(r"D:\MP74. Notificar Glosas Prestadores\04. Plantillas\REPORTE_DE_GLOSAS_BH_1.xlsx", index=False)
            print("El archivo no existe.")
        return 2
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e)   
    
print(noReporte())