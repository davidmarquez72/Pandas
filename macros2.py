from datetime import datetime, timedelta   
import os
import sys
import pandas as pd
import openpyxl
current_date = datetime.now().strftime('%d-%m-%Y')

def ClasTiem():
    try:       

        # Ruta dinámica para el archivo de pendientes
        ruta_pend3 = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', "Process\Pendientes3.xlsx")

        # Leer el archivo de pendientes "Pendientes2.xlsx" en un DataFrame
        df_pend3 = pd.read_excel(ruta_pend3)

        # Ruta para leer Hoja1 de Plantilla_ESTADO DE PENDIENTES A NIVEL NACIONAL 5.0 MODIFICADA1.xlsxm
        ruta_H1 = os.path.join('D:\RPA\AA\MP06. Pendientes\Plantillas\Hoja1.xlsx')

        # Leer el archivo de pendientes "Pendientes2.xlsx" en un DataFrame
        df_H1 = pd.read_excel(ruta_H1)

        # cruce entre pend3 y Hoja1, donde se busque "Sucursal de Radicación" del archivo1 en el archivo2 en la columna "OFICINAS DE RADICACION" donde se encuentre devuelve el valor de la columna "PROCESO OPORTUNIDAD"
        # cruce clasificacion 
        Cruce = pd.merge(df_pend3, df_H1[['OFICINAS DE RADICACION', 'PROCESO OPORTUNIDAD']],
                                left_on='Sucursal de Radicación', right_on='OFICINAS DE RADICACION', how='left')

        # Nueva columna 
        new_column_name = "Clasificación"
        column_index = df_pend3.columns.get_loc("Nivel De Autorización Del Procedimiento O Medicamento") + 1
        df_pend3.insert(column_index, new_column_name, "")

        # Asignar el valor de la columna "PROCESO OPORTUNIDAD" al "Clasificación" del archivo1
        df_pend3['Clasificación'] = Cruce['PROCESO OPORTUNIDAD']

        # Nueva columna 
        new_column_name = "Tiempos"
        column_index = df_pend3.columns.get_loc("Clasificación") + 1
        df_pend3.insert(column_index, new_column_name, "")

        # Definir una función para etiquetar los días
        def etiquetar_dias(dias):
            if 0 <= dias <= 1:
                return "0 - 1 Día"
            elif 2 <= dias <= 3:
                return "2 - 3 Días"
            elif 4 <= dias <= 10:
                return "4 - 10 Días"
            else:
                return "11 Días o más días"

        # Aplicar la función a la columna "Dias" y asignar los resultados a la columna "tiempos"
        df_pend3["Tiempos"] = df_pend3["Dias"].apply(etiquetar_dias)

        # ruta_pendtxt =  os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', "Process\ResultadosPendientes1.csv")
        ruta_pend4 = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', "Process\Pendientes4.xlsx")
        #ruta_pend4 = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs\29-07-2023\Process\Pendientes3.xlsx')


        # df_pend3.to_csv(ruta_pendtxt, sep='|', index=False, encoding='latin-1')
        df_pend3.to_excel(ruta_pend4, index=False)
        return 2
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e)   

print(ClasTiem())

def Categorizacion():
    try:
        # Ruta dinámica para el archivo de pendientes
        #ruta_pend3 = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs\29-07-2023\Process\Pendientes3.xlsx')
        ruta_pend4 = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', "Process\Pendientes4.xlsx")
        #ruta_pend3 = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', "Process\Pendientes3.xlsx")
        # Leer el archivo de pendientes "Pendientes2.xlsx" en un DataFrame
        df_pend4 = pd.read_excel(ruta_pend4)
        # -----------------------------------
        # Ruta para leer Hoja1 de Plantilla_ESTADO DE PENDIENTES A NIVEL NACIONAL 5.0 MODIFICADA1.xlsxm
        ruta_H1 = os.path.join('D:\RPA\AA\MP06. Pendientes\Plantillas\Hoja1.xlsx')
        # Leer el archivo de pendientes "Pendientes2.xlsx" en un DataFrame
        df_H1 = pd.read_excel(ruta_H1)
        # ------------------------------------
        # Ruta para leer Hoja3 de Plantilla_ESTADO DE PENDIENTES A NIVEL NACIONAL 5.0 MODIFICADA1.xlsxm
        ruta_H3 = os.path.join('D:\RPA\AA\MP06. Pendientes\Plantillas\Hoja3.xlsx')
        # Leer el archivo de pendientes "Pendientes2.xlsx" en un DataFrame
        df_H3 = pd.read_excel(ruta_H3)


        # Nueva columna 
        new_column_name = "Categorización"
        column_index = df_pend4.columns.get_loc("Tiempos") + 1
        df_pend4.insert(column_index, new_column_name, "")

        # Definimos una función auxiliar para aplicar las condiciones y búsquedas
        def categorizar(row):
            if row["PENDIENTES/JUNTAS/AHC"] == "JUNTAS":
                return "JUNTAS"
            elif row["Tipo de Servicio"] == "MEDICAMENTOS":
                return "SUPERVISOR"
            elif row["Nivel De Autorización Del Procedimiento O Medicamento"] in ["NIVEL 2 (FUNCIONARIO PROFESIONAL EN SALUD)", "NIVEL 3 (FUNCIONARIO PROFESIONAL EN SALUD)"]:
                return "SUPERVISOR"
            elif row["Código de la Prestación ó Medicamento"] in df_H3["CODIGO OSI"].values:
                return df_H3.loc[df_H3["CODIGO OSI"] == row["Código de la Prestación ó Medicamento"], "ASESOR/SUPERVISOR"].iloc[0]
            elif row["Nivel De Autorización Del Procedimiento O Medicamento"] == "NIVEL 4 (FUNCIONARIO PROFESIONAL EN SALUD)":
                return "ASESOR MEDICO"
            elif (row["Nivel De Autorización Del Procedimiento O Medicamento"] == "NIVEL 3 (FUNCIONARIO PROFESIONAL EN SALUD)") and (row["Servicio"] == "MEDICAMENTOS"):
                return "SUPERVISOR"
            elif row["Nivel De Autorización Del Procedimiento O Medicamento"] == "NIVEL 3 (FUNCIONARIO PROFESIONAL EN SALUD)":
                return df_H3.loc[df_H3["Nivel De Autorización Del Procedimiento O Medicamento"] == row["Nivel De Autorización Del Procedimiento O Medicamento"], "ATIENDE"].iloc[0]
            else:
                try:
                    return df_H3.loc[df_H3["CODIGO OSI"] == row["Código de la Prestación ó Medicamento"], "ASESOR/SUPERVISOR"].iloc[0]
                except IndexError:
                    try:
                        return df_H1.loc[df_H1["Nivel"] == row["Nivel De Autorización Del Procedimiento O Medicamento"], "CATEGORIZACIÓN"].iloc[0]
                    except IndexError:
                        return "SUPERVISORES"

        # Aplicamos la función a la columna "Categorizacion" de df_pend4 para obtener los resultados
        df_pend4["Categorización"] = df_pend4.apply(categorizar, axis=1)
        # sobreescribir
        df_pend4.to_excel(ruta_pend4, index=False)
        return 2
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e)  

print(Categorizacion())

def filtroBogCO():
    try:

        # Ruta dinámica para el archivo de pendientes
        ruta_pend4 = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', "Process\Pendientes4.xlsx")
        # Leer el archivo de pendientes "Pendientes4.xlsx" en un DataFrame
        df_pend4 = pd.read_excel(ruta_pend4, engine='openpyxl')
        # -----------------------------------
        # Ruta para leer Hoja1 de Plantilla_ESTADO DE PENDIENTES A NIVEL NACIONAL 5.0 MODIFICADA1.xlsxm
        ruta_H1 = os.path.join('D:\RPA\AA\MP06. Pendientes\Plantillas\Hoja1.xlsx')
        # Leer el archivo de pendientes "Pendientes2.xlsx" en un DataFrame
        df_H1 = pd.read_excel(ruta_H1)

        # Nueva columna 
        new_column_name = "Filtro Asignación Bogotá"
        column_index = df_pend4.columns.get_loc("Categorización") + 1
        df_pend4.insert(column_index, new_column_name, "")

        # Función para aplicar la lógica y retornar "SI" o "NO" según el valor de "Descripcion Regional Sucursal IPS Prestador"
        def asignar_filtro(row):
            if row["Descripcion Regional Sucursal IPS Prestador"] == "REGIONAL BOGOTA":
                return "SI"
            else:
                return "NO"

        # Aplicar la función a la columna "Filtro Asignación Bogotá"
        df_pend4["Filtro Asignación Bogotá"] = df_pend4.apply(asignar_filtro, axis=1)

        # Nueva columna 
        new_column_name = "Filtro Asignación Bogotá 2.0"
        column_index = df_pend4.columns.get_loc("Filtro Asignación Bogotá") + 1
        df_pend4.insert(column_index, new_column_name, "")

        # Realizar el cruce de los dataframes df_pen4 y df_H1 basado en la columna "Sucursal de Radicación"
        merged_df = pd.merge(df_pend4, df_H1, left_on="Sucursal de Radicación", right_on="FILTRO ASIGNACIÓN BOGOTA 2,0", how="left")

        # Asignar los valores de la columna "Asignacion Filtro" de df_H1 a la columna "Filtro Asignación Bogotá 2.0" de df_pen4
        df_pend4["Filtro Asignación Bogotá 2.0"] = merged_df["Asignacion Filtro"]

        # Reemplazar los valores NaN en la columna "Filtro Asignación Bogotá 2.0" por 0
        df_pend4["Filtro Asignación Bogotá 2.0"] = df_pend4["Filtro Asignación Bogotá 2.0"].fillna(0)

        # Nueva columna 
        new_column_name = "Filtro Asignación COriente"
        column_index = df_pend4.columns.get_loc("Filtro Asignación Bogotá 2.0") + 1
        df_pend4.insert(column_index, new_column_name, "")

        # Función para verificar las condiciones y asignar "SI" o "NO"
        def COriente(row):
            if row["Categorización"] == "SUPERVISOR" and row["Descripcion Ciudad de Sucursal IPS Prestador"] in df_H1["Ciudad de Radicacion"].values:
                return "SI"
            else:
                return "NO"

        # Aplicar la función a la columna "Filtro Asignación COriente" de df_pend4
        df_pend4["Filtro Asignación COriente"] = df_pend4.apply(lambda row: COriente(row), axis=1)

        # df_pend3.to_csv(ruta_pendtxt, sep='|', index=False, encoding='latin-1')
        df_pend4.to_excel(ruta_pend4, index=False)
        return 2
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e)     

print(filtroBogCO())

def consolidadoasignacion():
    try:
        # Ruta dinámica para el archivo de pendientes
        ruta_pend4 = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', "Process\Pendientes4.xlsx")
        # Leer el archivo de pendientes "Pendientes2.xlsx" en un DataFrame
        df_pend4 = pd.read_excel(ruta_pend4, engine='openpyxl')
        # -----------------------------------
        # Ruta para leer Hoja1 de Plantilla_ESTADO DE PENDIENTES A NIVEL NACIONAL 5.0 MODIFICADA1.xlsxm
        ruta_H1 = os.path.join('D:\RPA\AA\MP06. Pendientes\Plantillas\Hoja1.xlsx')
        # Leer el archivo de pendientes "Pendientes2.xlsx" en un DataFrame
        df_H1 = pd.read_excel(ruta_H1)

        # Nueva columna 
        new_column_name = "Consolidado"
        column_index = df_pend4.columns.get_loc("Filtro Asignación COriente") + 1
        df_pend4.insert(column_index, new_column_name, "")

        # Primero, definimos una función que aplicará las condiciones y retornará el valor correspondiente para la columna "Consolidado"
        def asignar_consolidado(row):
            if row["Filtro Asignación COriente"] == "SI":
                return "SI"
            elif row["Filtro Asignación Bogotá 2.0"] == "NO":
                return "NO"
            elif row["Filtro Asignación Bogotá 2.0"] == 0:
                return row["Filtro Asignación Bogotá"]
            else:
                return None  # Opcionalmente, podemos devolver un valor por defecto para los casos no cubiertos

        # Aplicamos la función a cada fila del DataFrame y actualizamos la columna "Consolidado"
        df_pend4["Consolidado"] = df_pend4.apply(asignar_consolidado, axis=1)

        # Nueva columna 
        new_column_name = "Asignación"
        column_index = df_pend4.columns.get_loc("Consolidado") + 1
        df_pend4.insert(column_index, new_column_name, "")

        # Definir una función que realice las asignaciones
        def asignar_asignacion(row):
            if row['PENDIENTES/JUNTAS/AHC'] == 'JUNTAS':
                return 'JUNTAS'
            elif row['Descripción Plan'] == 'COLSANITAS PLAN DENTAL':
                return 'COLSANITAS PLAN DENTAL'
            elif row['Tipo de Servicio'] == 'MEDICAMENTOS':
                return 'MEDICAMENTOS'
            elif row['PENDIENTES/JUNTAS/AHC'] == 'AHC':
                return 'AHC'
            elif row['Nivel De Autorización Del Procedimiento O Medicamento'] in df_H1['Nivel'].values:
                nivel = row['Nivel De Autorización Del Procedimiento O Medicamento']
                return df_H1[df_H1['Nivel'] == nivel]['CATEGORIZACIÓN'].iloc[0]
            else:
                return None

        # Aplicar la función a la columna "Asignación" del DataFrame df_pend4
        df_pend4['Asignación'] = df_pend4.apply(asignar_asignacion, axis=1)

        # update archivo
        df_pend4.to_excel(ruta_pend4, index=False)
        return 2
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e)      

print(consolidadoasignacion())

def filtroBogota():
    try:

        # Ruta dinámica para el archivo de pendientes
        ruta_pend4 = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', "Process\Pendientes4.xlsx")
        # Leer el archivo de pendientes "Pendientes2.xlsx" en un DataFrame
        df_pend4 = pd.read_excel(ruta_pend4, engine='openpyxl')
        # ------------------------------------
        # Ruta para leer Hoja3 de Plantilla_ESTADO DE PENDIENTES A NIVEL NACIONAL 5.0 MODIFICADA1.xlsxm
        ruta_H3 = os.path.join('D:\RPA\AA\MP06. Pendientes\Plantillas\Hoja3.xlsx')
        # Leer el archivo de pendientes "Pendientes2.xlsx" en un DataFrame
        df_H3 = pd.read_excel(ruta_H3)

        # Nueva columna 
        new_column_name = "Filtro para asignar Bogotá"
        column_index = df_pend4.columns.get_loc("Asignación") + 1
        df_pend4.insert(column_index, new_column_name, "")

        # Definir las condiciones
        cond1 = df_pend4["Sucursal de Radicación"].isin(["BACK OFFICE HOSPITALARIO BOGOTA", "OTROS BACK COLSANITAS EN LINEA", "AUTORIZACION TELEFONICA SM"])
        cond2 = df_pend4["Categorización"].isin(["JUNTAS", "AHC", "SUPERVISORES", "ASESOR MEDICO", "MEDICAMENTOS", "COLSANITAS PLAN DENTAL"])

        # Aplicar las condiciones para obtener los valores de la columna "ASIGNACIÓN2" de df_H3 en el DataFrame "df_pend4"
        df_pend4["Filtro para asignar Bogotá"] = df_pend4.apply(lambda row: df_H3.loc[df_H3["Fecha de Grabación de la Observación"] == row["Fecha de Grabación de la Observación"], "ASIGNACIÓN2"].values[0] if row["Sucursal de Radicación"] in cond1 and row["Fecha de Grabación de la Observación"] in cond2 else "ASIGNAR BOGOTÁ", axis=1)

        # Nueva columna 
        new_column_name = "Filtro Bogotá #2"
        column_index = df_pend4.columns.get_loc("Filtro para asignar Bogotá") + 1
        df_pend4.insert(column_index, new_column_name, "")

        # Realizar el cruce y actualización
        for index, row in df_pend4.iterrows():
            codigo = row['Código de la Prestación ó Medicamento']
            filtro = df_H3[df_H3['Codigo CUPS para excluir de odontologia'] == codigo]['ASIGNACIÓN CODIGO']
            
            if not filtro.empty:
                df_pend4.at[index, 'Filtro Bogotá #2'] = filtro.iloc[0]
            else:
                df_pend4.at[index, 'Filtro Bogotá #2'] = 'ASIGNAR'

        # update archivo
        df_pend4.to_excel(ruta_pend4, index=False)
        #print(filtroBogota())

        return 2
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e)         

print(filtroBogota())

def asigRegionalesProcessBogota():
    try:
        
        #current_date = datetime.now().strftime('%d-%m-%Y')

        # Ruta dinámica para el archivo de pendientes
        ruta_pend4 = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', "Process\Pendientes4.xlsx")
        # Leer el archivo de pendientes "Pendientes2.xlsx" en un DataFrame
        df_pend4 = pd.read_excel(ruta_pend4, engine='openpyxl')
        # ------------------------------------
        # Ruta para leer Hoja3 de Plantilla_ESTADO DE PENDIENTES A NIVEL NACIONAL 5.0 MODIFICADA1.xlsxm
        ruta_H3 = os.path.join('D:\RPA\AA\MP06. Pendientes\Plantillas\Hoja3.xlsx')
        # Leer el archivo de pendientes "Pendientes2.xlsx" en un DataFrame
        df_H3 = pd.read_excel(ruta_H3)

        # Nueva columna 
        new_column_name = "Asignacion Regionales"
        column_index = df_pend4.columns.get_loc("Filtro Bogotá #2") + 1
        df_pend4.insert(column_index, new_column_name, "")

        # Realizar el cruce y actualización
        for index, row in df_pend4.iterrows():
            sucursal = row['Sucursal de Radicación']
            asignacion = df_H3[df_H3['Sucursal de Radicación'] == sucursal]['Asignación sucursal']
            
            if not asignacion.empty:
                df_pend4.at[index, 'Asignacion Regionales'] = asignacion.iloc[0]
            else:
                df_pend4.at[index, 'Asignacion Regionales'] = 'ASIGNAR'

        # Nueva columna 
        new_column_name = "Asignación Procesos Bogotá"
        column_index = df_pend4.columns.get_loc("Asignacion Regionales") + 1
        df_pend4.insert(column_index, new_column_name, "")

        for index, row in df_pend4.iterrows():
            asignacion = row['Asignación']
            
            if asignacion == 'JUNTAS':
                df_pend4.at[index, 'Asignación Procesos Bogotá'] = 'JUNTAS'
            elif asignacion == 'COLSANITAS PLAN DENTAL' or asignacion == 'MEDICAMENTOS':
                df_pend4.at[index, 'Asignación Procesos Bogotá'] = asignacion
            elif row['PENDIENTES/JUNTAS/AHC'] == 'AHC':
                df_pend4.at[index, 'Asignación Procesos Bogotá'] = row['Categorización']
            else:
                codigo_pend4 = row['Código de la Prestación ó Medicamento']
                filtro_osi = df_H3[df_H3['CODIGO OSI'] == codigo_pend4]['ASESOR/SUPERVISOR']
                
                if not filtro_osi.empty:
                    df_pend4.at[index, 'Asignación Procesos Bogotá'] = filtro_osi.iloc[0]
                else:
                    df_pend4.at[index, 'Asignación Procesos Bogotá'] = row['Categorización']

        # update archivo
        df_pend4.to_excel(ruta_pend4, index=False)

        return 2
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e)       

print(asigRegionalesProcessBogota())

def asignprocesoDiasJuntas():
    try:
        
        #current_date = datetime.now().strftime('%d-%m-%Y')

        # Ruta dinámica para el archivo de pendientes
        ruta_pend4 = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', "Process\Pendientes4.xlsx")
        # Leer el archivo de pendientes "Pendientes2.xlsx" en un DataFrame
        df_pend4 = pd.read_excel(ruta_pend4, engine='openpyxl')

        # Nueva columna 
        new_column_name = "Asignación Por Proceso"
        column_index = df_pend4.columns.get_loc("Asignación Procesos Bogotá") + 1
        df_pend4.insert(column_index, new_column_name, "")

        # Aplicar la lógica y actualizar la columna "Asignación Por Proceso"
        for index, row in df_pend4.iterrows():
            if row['PENDIENTES/JUNTAS/AHC'] == 'AHC':
                df_pend4.at[index, 'Asignación Por Proceso'] = row['Asignación Procesos Bogotá'] + ' AHC'
            else:
                df_pend4.at[index, 'Asignación Por Proceso'] = row['Asignación Procesos Bogotá']

        # Nueva columna 
        new_column_name = "Dias Juntas"
        column_index = df_pend4.columns.get_loc("Asignación Por Proceso") + 1
        df_pend4.insert(column_index, new_column_name, "")

        # Aplicar las condiciones y actualizar la columna "Dias Juntas"
        for index, row in df_pend4.iterrows():
            dias = row['Dias']
            if dias <= 5:
                df_pend4.at[index, 'Dias Juntas'] = '0-5 días'
            elif 6 <= dias <= 10:
                df_pend4.at[index, 'Dias Juntas'] = '6-10 días'
            elif 11 <= dias <= 15:
                df_pend4.at[index, 'Dias Juntas'] = '11-15 días'
            else:
                df_pend4.at[index, 'Dias Juntas'] = 'Mayor 15 días'

        # df_pend3.to_csv(ruta_pendtxt, sep='|', index=False, encoding='latin-1')
        df_pend4.to_excel(ruta_pend4, index=False)
        return 2
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e)     

print(asignprocesoDiasJuntas())

def filtrosfinales():
    try:
              
        #print(filtrosfinales())
        #current_date = datetime.now().strftime('%d-%m-%Y')

        # Ruta dinámica para el archivo de pendientes
        ruta_pend4 = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', "Process\Pendientes4.xlsx")
        # Leer el archivo de pendientes "Pendientes2.xlsx" en un DataFrame
        df_pend4 = pd.read_excel(ruta_pend4, engine='openpyxl')
        
        # filtro 6.13
        # si en columna "Categorización" tiene “ASESOR MEDICO” y en la columna "Asignación Procesos Bogotá" tiene "SUPERVISOR", actualizar la columna "Categorización" con “ASESOR MEDICO” del df_pend4
        mask1 = (df_pend4['Categorización'] == 'ASESOR MEDICO') & (df_pend4['Asignación Procesos Bogotá'] == 'SUPERVISOR')
        df_pend4.loc[mask1, 'Categorización'] = 'ASESOR MEDICO'

        # filtro 6.14
        # si en columna "Categorización" tiene “SUPERVISOR” y en la columna "Asignación Procesos Bogotá" tiene "ASESOR MEDICO", actualizar la columna "Categorización" con “SUPERVISOR” del df_pend4
        mask2 = (df_pend4['Categorización'] == 'SUPERVISOR') & (df_pend4['Asignación Procesos Bogotá'] == 'ASESOR MEDICO')
        df_pend4.loc[mask2, 'Categorización'] = 'SUPERVISOR'

        # filtro 6.15
        # si en columna "Descripción de la Prestación o Médicamento" contiene la palabra “BIOMETRIA”, actualizar la columna "Categorización" con “ASESOR MEDICO” y actualizar la columna "Asignación Procesos Bogotá" con “ASESOR MEDICO” del df_pend4
        # Crear una máscara booleana para identificar las filas con "BIOMETRIA" en la descripción
        mask_biometria = df_pend4['Descripción de la Prestación o Médicamento'].str.contains('BIOMETRIA', case=False).fillna(False)
        # Actualizar las columnas correspondientes donde la máscara sea verdadera
        df_pend4.loc[mask_biometria, 'Categorización'] = 'ASESOR MEDICO'
        df_pend4.loc[mask_biometria, 'Asignación Procesos Bogotá'] = 'ASESOR MEDICO'

        # filtro 6.16
        # si en columna "Código de la Prestación ó Medicamento" tiene el codigo “1006007”, actualizar la columna "Categorización" con “SUPERVISOR” y actualizar la columna "Asignación Procesos Bogotá" con “SUPERVISOR” del df_pend4
        # Crear una máscara booleana para identificar las filas con el código "1006007"
        mask_codigo = df_pend4['Código de la Prestación ó Medicamento'] == 1006007

        # Actualizar las columnas correspondientes donde la máscara sea verdadera
        df_pend4.loc[mask_codigo, 'Categorización'] = 'SUPERVISOR'
        df_pend4.loc[mask_codigo, 'Asignación Procesos Bogotá'] = 'SUPERVISOR'


        df_pend4.to_excel(ruta_pend4, index=False)
        return 2
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e)     

print(filtrosfinales())