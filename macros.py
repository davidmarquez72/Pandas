from datetime import datetime, timedelta   
import os
import sys
import pandas as pd

def macrodias():
    try:   
                
        # Obtener la fecha actual
        fecha_actual = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

        # Ruta dinámica para el archivo de pendientes
        current_date = datetime.now().strftime('%d-%m-%Y')
        ruta_pend2 = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', "Process\Pendientes2.xlsx")

        # Leer el archivo de pendientes "Pendientes2.xlsx" en un DataFrame
        df_pend3 = pd.read_excel(ruta_pend2)

        # Ruta dinámica para el archivo de festivos
        ruta_festivo = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Plantillas\Festivos.xlsx')

        # Leer el archivo "festivos.xlsx" con las fechas festivas
        df_festivos = pd.read_excel(ruta_festivo)

        # Convertir la columna de fechas festivas al formato 'dd/mm/yyyy'
        df_festivos['FESTIVOS'] = pd.to_datetime(df_festivos['FESTIVOS'], format='%d/%m/%Y')

        # Convertir la columna "Fecha Expedición" al formato 'dd/mm/yyyy'
        df_pend3['Fecha Expedición'] = pd.to_datetime(df_pend3['Fecha Expedición'], format='%d/%m/%Y')

        # Crear una lista con las fechas festivas
        festivos_list = df_festivos["FESTIVOS"].dt.date.tolist()

        # Función para calcular los días laborables excluyendo los festivos
        def calcular_dias_laborables(fecha_inicio, fecha_fin, festivos_list):
            dias_laborables = 0
            fecha = fecha_inicio
            while fecha <= fecha_fin:
                if fecha.weekday() < 5 and fecha.date() not in festivos_list:
                    dias_laborables += 1
                fecha += timedelta(days=1)

            return dias_laborables -1

        # Calcular los días laborables para cada fecha de expedición
        df_pend3["Dias"] = df_pend3.apply(lambda row: calcular_dias_laborables(row["Fecha Expedición"], fecha_actual, festivos_list), axis=1)

        # Convertir la columna "Fecha Expedición" nuevamente al formato 'dd/mm/yyyy'
        df_pend3['Fecha Expedición'] = df_pend3['Fecha Expedición'].dt.strftime('%d/%m/%Y')

        # Ordenar el DataFrame por 'Número de Autorización'
        df_pend3 = df_pend3.sort_values(by='Número de Autorización', ascending=True)

        # Ruta dinámica para el archivo resultante de pendientes
        ruta_pend3 = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', "Process\Pendientes3.xlsx")

        # Guardar el resultado en el archivo "Pendientes3.xlsx"
        df_pend3.to_excel(ruta_pend3, index=False)
                
        return 2
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e)         


def diasAntiguedad():
    try:
        
        # Ruta dinámica para el archivo de pendientes
        current_date = datetime.now().strftime('%d-%m-%Y')
        ruta_pend3 = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', "Process\Pendientes3.xlsx")

        # Leer el archivo de pendientes "Pendientes2.xlsx" en un DataFrame
        df_pend3 = pd.read_excel(ruta_pend3)

        # Ruta dinámica para el archivo de festivos
        ruta_festivo = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Plantillas\Festivos.xlsx')

        # Leer el archivo "festivos.xlsx" con las fechas festivas
        df_festivos = pd.read_excel(ruta_festivo)


        # Crear una función para asignar los días de antiguedad desde el DataFrame "festivos"
        def asignar_antiguedad(dias):
            if dias > 50:
                return "Mayores a 50 días"
            elif dias in df_festivos["DIAS"].values:
                return df_festivos.loc[df_festivos["DIAS"] == dias, "DIAS DE ANTIGUEDAD"].values[0]
            else:
                return None

        # Aplicar la función a la columna "dias" del DataFrame "pendientes"
        df_pend3["Dias de antiguedad"] = df_pend3["Dias"].apply(asignar_antiguedad)

        # Guardar el resultado en el archivo "Pendientes3.xlsx"
        df_pend3.to_excel(ruta_pend3, index=False)

        return 2
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e) 

def oportunidad():
    try:
        # Ruta dinámica para el archivo de pendientes
        current_date = datetime.now().strftime('%d-%m-%Y')
        ruta_pend3 = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', "Process\Pendientes3.xlsx")

        # Leer el archivo de pendientes "Pendientes2.xlsx" en un DataFrame
        df_pend3 = pd.read_excel(ruta_pend3)

        # Función para determinar la oportunidad
        def determinar_oportunidad(row):
            if row["Descripción Plan"] == "COLSANITAS PLAN DENTAL" and row["Dias"] <= 2:
                return "OPORTUNO"
            elif row["PENDIENTES/JUNTAS/AHC"] == "AHC":
                return "INOPORTUNO" if row["Dias"] > 3 else "OPORTUNO"
            elif row["PENDIENTES/JUNTAS/AHC"] == "JUNTAS":
                return "INOPORTUNO" if row["Dias"] >= 11 else "OPORTUNO"
            elif row["PENDIENTES/JUNTAS/AHC"] == "PENDIENTES":
                return "INOPORTUNO" if row["Dias"] > 1 else "OPORTUNO"
            else:
                return None

        ruta_pendtxt =  os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', "Process\ResultadosPendientes1.csv")

        # Aplicar la función a las columnas relevantes del DataFrame "pendientes"
        df_pend3["Oportunidad"] = df_pend3.apply(determinar_oportunidad, axis=1)
        df_pend3.to_csv(ruta_pendtxt, sep='|', index=False, encoding='latin-1')
        df_pend3.to_excel(ruta_pend3, index=False)
        return 2
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e)
