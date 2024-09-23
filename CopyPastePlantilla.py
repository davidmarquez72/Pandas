import sys
import pandas as pd
from datetime import datetime
import os
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows

def copy():
    try:
        
        # fecha actual
        current_date = datetime.now().strftime('%Y-%m-%d')

        # ruta dinamica
        ruta_info = os.path.join('D:/MP74. Notificar Glosas Prestadores/03. Output', f'{current_date}/Info.xlsx')
        ruta_plantilla = os.path.join('D:/MP74. Notificar Glosas Prestadores/03. Output', f'{current_date}/Reporte Glosas.xlsx')

        # Cargar el archivo Excel de origen en un DataFrame
        reporte = pd.read_excel(r"D:\MP74. Notificar Glosas Prestadores\04. Plantillas\REPORTE_DE_GLOSAS_BH_2.xlsx")

        # Seleccionar las columnas que se van a copiar
        columnas_a_copiar = reporte[[
            'PRODUCTO', 'NUMERO DE RADICACION', 'ID GLOSA', 'FECHA DE RADICACION', 'CLASE DE CUENTA', 'NUMERO IDENT PRESTADOR', 'NOMBRES PRESTADOR',
            'SUCURSAL IPS', 'NOMBRE DE LA SUCURSAL IPS', 'CIUDAD DEL PRESTADOR', 'NUMERO DE FACTURA', 'NIVEL GLOSA', 'FECHA ATENCION', 'TIPO ATENCION',
            'TIPO IDENT AFILIADO', 'NUMERO IDENT AFILIADO', 'NOMBRE AFILIADO', 'PLAN', 'CODIGO PROCEDIMIENTO', 'NOMBRE PROCEDIMIENTO', 'CODIGO HOMOLOGO', 
            'NOMBRE HOMOLOGO', 'NOMBRE CONCEPTO NORMAL', 'NOMBRE CONCEPTO ADICIONAL', 'CÓDIGO MEDICAMENTO E INSUMO IPS', 'DESCRIPCIÓN MEDICAMENTO E INSUMO IPS',
            'TIPO DE SERVICIO', 'VALOR TOTAL NEGOCIADO GLOSA', 'PORCENTAJE IVA', 'VALOR IVA', 'VALOR FACTURADO GLOSA', 'VALOR GLOSADO GLOSA', 'VALOR IVA GLOSA', 
            'VALOR GLOSADO PRESTADOR', 'VALOR REAL GLOSA', 'CODIGO CAPITULO', 'CAPITULO', 'CODIGO SUBCAPITULO', 'SUBCAPITULO', 'OBSERVACIONES',
            ]]

        # eliminar columnas vacias
        # columna_fin = columnas_a_copiar.dropna(axis=1, how='all')

        # Cargar la plantilla de Excel en un DataFrame
        plantilla = pd.read_excel(ruta_info)
        fin = pd.DataFrame(columnas_a_copiar)
        fin.to_excel(ruta_info, index=False)

        # Leer la plantilla de Excel
        wb = openpyxl.load_workbook(ruta_plantilla)
        sheet = wb['Hoja1']
        
        return 2

    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e)

