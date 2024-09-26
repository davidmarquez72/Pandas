import sys
import pandas as pd
import os
from datetime import datetime
import numpy as np

def asignacion():
    try:        
        # fecha actual
        current_date = datetime.now().strftime('%d-%m-%Y')

        # ruta dinamica
        ruta_pendietes = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', "Process\Pendientes_Archivo_Plano.txt")
        #ruta_pendietes = r'D:\RPA\AA\MP06. Pendientes\Outputs\17-07-2023\Process\Pendientes_Archivo_Plano.txt'

        # pasar a dataframe archivo txt
        df_pendientes = pd.read_csv(ruta_pendietes, sep = '|',encoding='latin-1',low_memory=False)

        # Definir condiciones y valores correspondientes
        condiciones = [(df_pendientes['Código Observación'].eq(505) | df_pendientes['Código Observación'].eq(506)),
                (df_pendientes['Código Observación'].eq(509) | df_pendientes['Código Observación'].eq(510))]
        valores = ['AHC', 'JUNTAS']

        # Asignar 'PENDIENTES' para el resto de los casos
        df_pendientes['Número de Evento'] = np.select(condiciones, valores, default='PENDIENTES')

        # Ordenar el DataFrame en la columna 'Número de autorización' de forma ascendente
        df_pendientes = df_pendientes.sort_values(by='Número de Autorización', ascending=True)

        # Ordenar Pendientes_Original por "Numero de Evento" y eliminar duplicados por "Numero de Autorizacion"
        df_Pendientes_OrdenEvento = df_pendientes.sort_values(by="Número de Evento", key=lambda col: col.map({'JUNTAS': 0,\
                                                                                                            'AHC': 1,\
                                                                                                            'PENDIENTES': 2})).drop_duplicates(subset="Número de Autorización")

        # seleccionar solo numero de autorizacion y nivel de autorizacion
        df_pendientes_Nivel = df_pendientes[['Número de Autorización','Nivel de Autorización']]

        # Ordenar Pendientes por "Nivel de Autorizacion" y eliminar duplicados por "Numero de Autorizacion"
        df_Pendientes_OrdeNivel = df_pendientes_Nivel.sort_values(by="Nivel de Autorización", key=lambda col: col.map({'NIVEL 4 (FUNCIONARIO PROFESIONAL EN SALUD)': 0,\
                                                                                                                        'NIVEL 3 (FUNCIONARIO PROFESIONAL EN SALUD)': 1,\
                                                                                                                        'NIVEL 2 (FUNCIONARIO PROFESIONAL EN SALUD)': 2,\
                                                                                                                        'NIVEL 1 (FUNCIONARIO NIVEL BASICO)': 3, \
                                                                                                                        '': 4})).drop_duplicates(subset="Número de Autorización")

        # Realizar INNER JOIN en "Numero de Autorizacion" entre los DataFrames previamente creados
        df_Pendientes_Final = pd.merge(df_Pendientes_OrdenEvento, df_Pendientes_OrdeNivel, on="Número de Autorización", how="inner")

        # cambiar columna nivel de autorizacion
        autorizacion = df_Pendientes_Final['Nivel de Autorización_y']
        df_Pendientes_Final['Nivel de Autorización_x'] = autorizacion
        df_Pendientes_Final.rename(columns={'Nivel de Autorización_x': 'Nivel de Autorización'}, inplace=True)

        # eliminar columnas no necesarias
        df_Pendientes_Final.drop(columns=['Nivel de Autorización_y','Nombre del Medicamento Comodín','Nombre Comercial Comodín', 'Forma Farmaceutica Comodín',\
                                        'Concentración Comodín','Cantidad Comodín','Código Canal de radicación','Estado Autorización'], inplace=True)

        # ruta dinamica
        ruta_pend = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', "Process\Pendientes.xlsx")
        #ruta_pendtxt =  os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', "Process\Pendientes.csv")

        # df a excel
        df_Pendientes_Final.to_excel(ruta_pend, index=False)
        #df_Pendientes_Final.to_csv(ruta_pendtxt, sep='|', index=False, encoding='latin-1')

        return 2
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e)

print(asignacion())