import sys
import pandas as pd
import os
from datetime import datetime   

def template():
    try:
        # fecha actual
        current_date = datetime.now().strftime('%d-%m-%Y')

        # ruta dinamica pendientes
        ruta_pend = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', "Process\Pendientes.xlsx")

        # pasar a dataframe archivo 
        df_pend2 = pd.read_excel(ruta_pend)
        # -----------------------------------
        # pasar a tipo de dato datatime
        df_pend2['Fecha de Grabación'] = pd.to_datetime(df_pend2['Fecha de Grabación'], format='%d/%m/%Y')

        # Crear una nueva columna "Año" y extraer el año de la columna "Fecha grabacion"
        df_pend2['Año Exped'] = df_pend2['Fecha de Grabación'].dt.year

        # Crear una nueva columna "Mes" y extraer el mes de la columna "Fecha grabacion"
        df_pend2["Mes de grabación"] = df_pend2["Fecha de Grabación"].dt.month

        # Si deseas que el mes sea representado con el nombre, puedes hacer lo siguiente:
        df_pend2["Mes de grabación"] = df_pend2["Fecha de Grabación"].dt.strftime("%B")  # %B representa el nombre completo del mes
        # -----------------------------------
        # Crear la nueva columna "Descripcion Regional Sucursal IPS Prestador" con los mismos valores de "Regional Sucursal IPS Prestador"
        df_pend2["Descripcion Regional Sucursal IPS Prestador"] = df_pend2["Regional Sucursal IPS Prestador"]

        # ----------------------------------- 
        # Crear la nueva columna "Descripcion Ciudad de Sucursal IPS Prestador" con los mismos valores de "Ciudad de Sucursal IPS Prestador"
        df_pend2["Descripcion Ciudad de Sucursal IPS Prestador"] = df_pend2["Ciudad de Sucursal IPS Prestador"]

        # -----------------------------------
        # pasar a tipo de dato datatime Fecha Expedición
        df_pend2['Fecha Expedición'] = pd.to_datetime(df_pend2['Fecha Expedición'], format='%d/%m/%Y %H:%M:%S')
        # pasar fecha de expedicion en formato "dd/mm/yyyy"
        df_pend2['Fecha Expedición'] = df_pend2['Fecha Expedición'].dt.strftime('%d/%m/%Y')
        # -----------------------------------
        # pasar a tipo de dato datatime Fecha de Solicitud
        df_pend2['Fecha de Solicitud'] = pd.to_datetime(df_pend2['Fecha de Solicitud'], format='%d/%m/%Y %H:%M:%S')
        # pasar Fecha de Solicitud en formato "dd/mm/yyyy"
        df_pend2['Fecha de Solicitud'] = df_pend2['Fecha de Solicitud'].dt.strftime('%d/%m/%Y')

        # -----------------------------------
        # pasar a tipo de dato datatime Fecha límite de Gestión
        df_pend2['Fecha límite de Gestión'] = pd.to_datetime(df_pend2['Fecha límite de Gestión'], format='%d/%m/%Y %H:%M:%S')
        # pasar Fecha límite de Gestión en formato "dd/mm/yyyy"
        df_pend2['Fecha límite de Gestión'] = df_pend2['Fecha límite de Gestión'].dt.strftime('%d/%m/%Y')

        # -----------------------------------
        # pasar a tipo de dato datatime Fecha Fecha de Grabación de la Observación
        df_pend2['Fecha de Grabación de la Observación'] = pd.to_datetime(df_pend2['Fecha de Grabación de la Observación'], format='%d/%m/%Y %H:%M:%S')
        # pasar Fecha de Grabación de la Observación en formato "dd/mm/yyyy"
        df_pend2['Fecha de Grabación de la Observación'] = df_pend2['Fecha de Grabación de la Observación'].dt.strftime('%d/%m/%Y')

        # -----------------------------------
        # pasar a tipo de dato datatime Fecha Fecha de Generación del Reporte
        df_pend2['Fecha de Generación del Reporte'] = pd.to_datetime(df_pend2['Fecha de Generación del Reporte'], format='%d/%m/%Y %H:%M:%S')
        # pasar Fecha de Generación del Reporte en formato "dd/mm/yyyy"
        df_pend2['Fecha de Generación del Reporte'] = df_pend2['Fecha de Generación del Reporte'].dt.strftime('%d/%m/%Y')

        # ----------------------------------- 
        # Crear la nueva columna "PENDIENTES/JUNTAS/AHC" con los mismos valores de "Número de Evento"
        df_pend2["PENDIENTES/JUNTAS/AHC"] = df_pend2["Número de Evento"]

        # ----------------------------------- 
        # Crear la nueva columna "Nivel De Autorización Del Procedimiento O Medicamento" con los mismos valores de "Nivel de Autorización"
        df_pend2["Nivel De Autorización Del Procedimiento O Medicamento"] = df_pend2["Nivel de Autorización"]

        # ------------------------------------------
        # pasar fecha en formato "dd/mm/yyyy"
        df_pend2['Fecha de Grabación'] = df_pend2['Fecha de Grabación'].dt.strftime('%d/%m/%Y')

        # ------------------------------------
        # Mover la columna "Año Exped" desde la última posición a la primera
        # columnas que se desean mover
        desired_columns = ["Año Exped", "Mes de grabación", "Descripcion Regional Sucursal IPS Prestador", "Descripcion Ciudad de Sucursal IPS Prestador" ]  # Replace these with the actual column names
        all_columns = df_pend2.columns.tolist()
        # Check de si existen esas columnas
        missing_columns = [col for col in desired_columns if col not in df_pend2.columns]
        if missing_columns:
            raise ValueError(f"The following columns are missing in the DataFrame: {missing_columns}")

        # Mover las columnas al principio
        for column in desired_columns[::-1]:
            all_columns.remove(column)
            all_columns.insert(0, column)

        # guardar las columnas
        df_pend2 = df_pend2[all_columns]

        # Nueva columna 
        new_column_name = "Dias"
        column_index = df_pend2.columns.get_loc("Mes de grabación") + 1
        df_pend2.insert(column_index, new_column_name, "")

        # Nueva columna 
        new_column_name = "Dias de antiguedad"
        column_index = df_pend2.columns.get_loc("Mes de grabación") + 1
        df_pend2.insert(column_index, new_column_name, "")

        # Nueva columna 
        new_column_name = "Oportunidad"
        column_index = df_pend2.columns.get_loc("PENDIENTES/JUNTAS/AHC") + 1
        df_pend2.insert(column_index, new_column_name, "")

        # ruta dinamica
        ruta_pend2 = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', "Process\Pendientes2.xlsx")

        # df a excel
        df_pend2.to_excel(ruta_pend2, index=False,engine='openpyxl')
        
        return 2
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e) 

print(template())