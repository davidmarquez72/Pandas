import sys
import pandas as pd
import os
from datetime import datetime


def CrucePlanoEps():
    try:
        # fecha actual
        current_date = datetime.now().strftime('%d-%m-%Y')

        # ruta dinamica pendientes
        ruta_Eps = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', f"Process\Pendientes_Archivo_EPS.txt")
        #ruta_Eps = r"D:\RPA\AA\MP06. Pendientes\Outputs\13-07-2023\Process\Pendientes_Archivo_EPS.txt"

        # pasar a dataframe archivo txt
        df_Eps = pd.read_csv(ruta_Eps, sep = '|',encoding='latin-1',low_memory=False)

        # ruta dinamica plano
        ruta_plano = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', f"Process\Archivo_Plano_EPS.txt")
        #ruta_plano = r"D:\RPA\AA\MP06. Pendientes\Outputs\13-07-2023\Process\Archivo_Plano_EPS.txt"

        # pasar a dataframe archivo txt
        df_plano = pd.read_csv(ruta_plano, sep = '|',encoding='latin-1',low_memory=False)

        # Seleccionar registros con "SI" en la columna "usuarios compartidos" de plano
        df_siplano = df_plano[df_plano['Clase de Usuario Compartido'] == 'SI']

        # agregar prefijo a df_siplano
        df_siplanopre = df_siplano.add_prefix('pla_')
        #df_Epspre = df_Eps.add_prefix('pla_')

        # Realizar cruce en la columna "Numero de autorizacion" entre lso seleccionados "si" y eps
        df_cruce = df_Eps.merge(df_siplanopre, left_on='Número de Autorización',right_on='pla_Número de Autorización', how='inner')[df_Eps.columns]
       
        # ruta dinamica process eps
        #ruta_pendientes_epsx = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', f"Process\cruce_EPS.xlsx")
        ruta_pendientes_eps = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', f"Process\cruce_EPS.txt")

        # resultado
        #df_cruce.to_excel(ruta_pendientes_epsx,index=False)
        df_cruce.to_csv(ruta_pendientes_eps, sep='|', index=False, encoding='latin-1')

        return 2
  
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e)
print(CrucePlanoEps())

def cruceLista():
    try:
       # fecha actual
        current_date = datetime.now().strftime('%d-%m-%Y')

        # ruta dinamica cruce eps
        ruta__cruceEps = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', f"Process\cruce_EPS.txt")

        # pasar a dataframe archivo txt
        df_cruceEps = pd.read_csv(ruta__cruceEps, sep = '|',encoding='latin-1',low_memory=False)

        # ruta para lista de oficinas a filtrar
        ruta_lista = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Inputs\SUCURSALES MP.xlsx')

        # pasar a dataframe archivo txt
        df_lista = pd.read_excel(ruta_lista)

        # Seleccionar registros con "SI" en la columna "usuarios compartidos" de plano
        #df_listselec = df_lista[df_lista['Para asignar'].str.contains('x', case=False)]
        df_listselec = df_lista[df_lista['Para asignar'] == 'x']

        # filtrar archivo cruceEPS
        df_filtrado= pd.merge(df_cruceEps, df_listselec, right_on='Sucursal', left_on='Sucursal de Radicación' , how='inner')

        # eliminar columna  
        df_filtrado = df_filtrado.drop(columns=['Para asignar'])

        # ruta res
        ruta_fin = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', f"Process\EPS.txt")
        ruta_fine = os.path.join(r'D:\RPA\AA\MP06. Pendientes\Outputs', f'{current_date}', f"Process\EPS.xlsx")

        # resultado
        
        df_filtrado.to_excel(ruta_fine,index=False)
        df_filtrado.to_csv(ruta_fin, sep='|', index=False, encoding='latin-1', float_format='%.0f')

        return 2
    
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e)
print(cruceLista())
