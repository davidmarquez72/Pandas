import sys
import pandas as pd
from datetime import datetime, timedelta
from openpyxl import load_workbook

def duplicados():
    try:
        # Leemos el archivo txt
        dftotal = pd.read_excel(r"D:\MP74. Notificar Glosas Prestadores\04. Plantillas\Union.xlsx")

        # buscamos los IDS GLOSAS duplicados 
        duplicated_ids = dftotal[dftotal.duplicated(subset='ID GLOSA', keep=False)]

        # guardamos los ids en un dataframe
        dfexcelnew = pd.DataFrame(duplicated_ids)

        # fecha actual
        current_date = datetime.now().strftime('%Y-%m-%d')

        # se guarda en un nuevo excel
        if dfexcelnew.empty:
            print("nothing")
        else:
            dfexcelnew.to_excel(f'D:/MP74. Notificar Glosas Prestadores/04. Plantillas/Duplicated_ID_GLOSAS_{current_date}.xlsx', index=False)
        return 2
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e)

def filtro(strDateSpecific):
    try:
        
        # fecha actual restar 1 dia
        current_date = datetime.now()
        sm1 = timedelta(1)
        current_date_1 = (current_date - sm1).strftime('%d/%m/%Y')

        
        # Leemos el archivo 
        ruta_union = r"D:\MP74. Notificar Glosas Prestadores\04. Plantillas\Union.xlsx"
        dftotal = pd.read_excel(ruta_union)

        # seleccionar todo COLSANITAS Y MEDISANITAS
        filtro = dftotal['PRODUCTO'].str.contains('COLSANITAS|MEDISANITAS', case=False)
        df_filtro = dftotal[filtro]
        # sobreescribir excel
        df_filtro.to_excel(ruta_union, index=False)

        # seleccionar enviado a tesoreria
        dftotal = pd.read_excel(ruta_union) 
        filtro = dftotal['ESTADO'].str.contains('ENVIADA A TESORERIA', case=False)
        df_filtro = dftotal[filtro]
        # sobreescribir excel
        df_filtro.to_excel(ruta_union, index=False)

        # seleccionar fecha de ayer en contabilizacion
        dftotal = pd.read_excel(ruta_union)

        if strDateSpecific != '':
            current_date_1 = strDateSpecific

        df_fitro_fecha = dftotal[dftotal['FECHA CONTABILIZACION']== current_date_1]
        df_fitro_fecha.to_excel(ruta_union, index=False)

        # Cargar el archivo de Excel
        wb = load_workbook(ruta_union)
        
        # Obtener la hoja de trabajo actual
        hoja = wb["Sheet1"]

        # Renombrar la hoja de trabajo
        hoja.title = "Hoja1"
            
        # Guardar los cambios en el archivo
        wb.save(ruta_union)
            
        # Cerrar el archivo
        wb.close()
        return 2
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e)

