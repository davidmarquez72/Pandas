from datetime import datetime, timedelta   
import os
import sys
import pandas as pd
from openpyxl import load_workbook
current_date = datetime.now().strftime('%d-%m-%Y')

def dashboard():
    try:        
        #ruta_pend4 = os.path.join(r'C:\Users\asistente2.SRVVKRPAEP4\Downloads\Pendientes4.xlsx')
        #ruta_info = os.path.join(r'C:\Users\asistente2.SRVVKRPAEP4\Downloads\info.xlsx')
        ruta_pend4 = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', "Process\Pendientes4.xlsx")
        ruta_info = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', "Process\info.xlsx")
        # Leer el archivo de pendientes "Pendientes2.xlsx" en un DataFrame
        df_pend4 = pd.read_excel(ruta_pend4)

        # Crear un nuevo DataFrame con las columnas deseadas
        columnas_deseadas = [
            'Año Exped',
            'Mes de grabación',
            'Dias de antiguedad',
            'Dias',
            'Descripcion Regional Sucursal IPS Prestador',
            'Descripcion Ciudad de Sucursal IPS Prestador',
            'Sucursal de Radicación',
            'Ciudad de Radicación',
            'Regional',
            'Número de Autorización',
            'Número de Evento',
            'Fecha de Grabación',
            'Usuario de Grabación',
            'Fecha Expedición',
            'Fecha de Solicitud',
            'Gestionar Pendiente',
            'Fecha límite de Gestión',
            'Días Pendientes',
            'Tipo Identificacion del Afiliado',
            'No Identificacion del Afiliado',
            'Nombres del Afiliado',
            'Descripción Producto',
            'Descripción Plan',
            'Contrato',
            'Tipo Identificación Remitente',
            'Identificacion Remitente',
            'Nombre Remitente',
            'Código Sucursal IPS Remitente',
            'Nombre Sucursal Remitente',
            'Tipo Identificación Prestador',
            'Identificacion Prestador',
            'Nombre Prestador',
            'Código Sucursal IPS Prestador',
            'Nombre Sucursal Prestador',
            'Tipo de Servicio',
            'Tipo de Atención',
            'Tipo de Radicación',
            'Servicio',
            'Código de la Prestación ó Medicamento',
            'Descripción de la Prestación o Médicamento',
            'Estado de la Prestación o Medicamento',
            'Cantidad',
            'Código Observación',
            'Descripción Observación',
            'Información Adicional de la Observación',
            'Imprimir de la Observación',
            'Sucursal de la Observación',
            'Usuario de la Observación',
            'Fecha de Grabación de la Observación',
            'Fecha de Generación del Reporte',
            'PENDIENTES/JUNTAS/AHC',
            'Oportunidad',
            'Nivel De Autorización Del Procedimiento O Medicamento',
            'Clasificación',
            'Tiempos',
            'Categorización',
            'Filtro Asignación Bogotá',
            'Filtro Asignación Bogotá 2.0',
            'Filtro Asignación COriente',
            'Consolidado',
            'Asignación',
            'Filtro para asignar Bogotá',
            'Filtro Bogotá #2',
            'Asignacion Regionales',
            'Asignación Procesos Bogotá',
            'Asignación Por Proceso',
            'Dias Juntas'
        ]
        nuevo_df = df_pend4[columnas_deseadas]
        nuevo_df.to_excel(ruta_info, header=False, index=False)
        return 2    
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e)  
    
print(dashboard())