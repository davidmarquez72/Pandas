import sys
import pandas as pd
from datetime import datetime, timedelta
import os

def clinicaDental():
    try:
        # fecha actual y sumar 1 dia
        current_date = datetime.now()
        current_date_hoy = datetime.now().strftime('%Y-%m-%d')
        sm1 = timedelta(1)
        current_date_1 = (current_date + sm1).strftime('%Y-%m-%d')

        # ruta citas
        ruta_citas = os.path.join(r'D:\MP68-Recordatorio de citas por Maria Maula\03.output',f'{current_date_hoy}',f'Citas Medicas Presenciales {current_date_1}.xlsx')
        #ruta_citas = r'D:\MP68-Recordatorio de citas por Maria Maula\Citas Medicas Presenciales 2023-08-01.xlsx'
        # lee archivo citas medicas presenciales fecha
        df_citas = pd.read_excel(ruta_citas)
        # ------------------------------------------------------ Clinica Dental  ---------------------------------------------------------
        # --------------------------------------------------------------------------------------------------------------------------------
        # Eliminar Ortodoncia
        df_citas = df_citas.loc[~((df_citas["Nombre de la sede"].str.contains("Clinica Dental", case=False)) & 
                            (df_citas["Nombre de la especialidad / procedimiento"].str.contains("Ortodoncia", case=False)))]
        # --------------------------------------------------------------------------------------------------------------------------------
        # Eliminar ortopedia maxilar
        df_citas = df_citas.loc[~((df_citas["Nombre de la sede"].str.contains("Clinica Dental", case=False)) & 
                            (df_citas["Nombre de la especialidad / procedimiento"].str.contains("ortopedia maxilar", case=False)))]
        # --------------------------------------------------------------------------------------------------------------------------------
        # Eliminar Rehabilitacion Oral
        df_citas = df_citas.loc[~((df_citas["Nombre de la sede"].str.contains("Clinica Dental", case=False)) & 
                            (df_citas["Nombre de la especialidad / procedimiento"].str.contains("Rehabilitacion Oral", case=False)))]
        # --------------------------------------------------------------------------------------------------------------------------------
        # Eliminar Periodoncia
        df_citas = df_citas.loc[~((df_citas["Nombre de la sede"].str.contains("Clinica Dental", case=False)) & 
                            (df_citas["Nombre de la especialidad / procedimiento"].str.contains("Periodoncia", case=False)))]
        # --------------------------------------------------------------------------------------------------------------------------------
        # Eliminar Odontologia General
        df_citas = df_citas.loc[~((df_citas["Nombre de la sede"].str.contains("Clinica Dental", case=False)) & 
                            (df_citas["Nombre de la especialidad / procedimiento"].str.contains("Odontologia General", case=False)))]
        # --------------------------------------------------------------------------------------------------------------------------------
        # Eliminar odontología general
        df_citas = df_citas.loc[~((df_citas["Nombre de la sede"].str.contains("Clinica Dental", case=False)) & 
                            (df_citas["Nombre de la especialidad / procedimiento"].str.contains("Odontologia General", case=False)))]
        # --------------------------------------------------------------------------------------------------------------------------------
        # Eliminar Endodoncia
        df_citas = df_citas.loc[~((df_citas["Nombre de la sede"].str.contains("Clinica Dental", case=False)) & 
                            (df_citas["Nombre de la especialidad / procedimiento"].str.contains("Endodoncia", case=False)))]
        # --------------------------------------------------------------------------------------------------------------------------------
        # Eliminar Cirugia Oral
        df_citas = df_citas.loc[~((df_citas["Nombre de la sede"].str.contains("Clinica Dental", case=False)) & 
                            (df_citas["Nombre de la especialidad / procedimiento"].str.contains("Cirugia Oral", case=False)))]
        # --------------------------------------------------------------------------------------------------------------------------------
        # Eliminar Odontologia Pediatrica
        df_citas = df_citas.loc[~((df_citas["Nombre de la sede"].str.contains("Clinica Dental", case=False)) & 
                            (df_citas["Nombre de la especialidad / procedimiento"].str.contains("Odontologia Pediatrica", case=False)))]
        

        # ruta guardar
        df_citas.to_excel(ruta_citas, index=False)
        #df_citas.to_excel(r'D:\MP68-Recordatorio de citas por Maria Maula\rta.xlsx', index=False)
        return 2
    
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e)

print(clinicaDental())

def Odontosanitas():
    try:
        # fecha actual y sumar 1 dia
        current_date = datetime.now()
        current_date_hoy = datetime.now().strftime('%Y-%m-%d')
        sm1 = timedelta(1)
        current_date_1 = (current_date + sm1).strftime('%Y-%m-%d')

        # ruta citas
        ruta_citas = os.path.join(r'D:\MP68-Recordatorio de citas por Maria Maula\03.output',f'{current_date_hoy}',f'Citas Medicas Presenciales {current_date_1}.xlsx')
        #ruta_citas = r'D:\MP68-Recordatorio de citas por Maria Maula\Citas Medicas Presenciales 2023-08-01.xlsx'
        # lee archivo citas medicas presenciales fecha
        df_citas = pd.read_excel(ruta_citas)
        # ------------------------------------------------------ Odontosanitas ---------------------------------------------------------
        # --------------------------------------------------------------------------------------------------------------------------------
        # Eliminar Ortodoncia
        df_citas = df_citas.loc[~((df_citas["Nombre de la sede"].str.contains("Odontosanitas", case=False)) & 
                            (df_citas["Nombre de la especialidad / procedimiento"].str.contains("Ortodoncia", case=False)))]
        # --------------------------------------------------------------------------------------------------------------------------------
        # Eliminar ortopedia maxilar
        df_citas = df_citas.loc[~((df_citas["Nombre de la sede"].str.contains("Odontosanitas", case=False)) & 
                            (df_citas["Nombre de la especialidad / procedimiento"].str.contains("ortopedia maxilar", case=False)))]
        # --------------------------------------------------------------------------------------------------------------------------------
        # Eliminar Rehabilitacion Oral
        df_citas = df_citas.loc[~((df_citas["Nombre de la sede"].str.contains("Odontosanitas", case=False)) & 
                            (df_citas["Nombre de la especialidad / procedimiento"].str.contains("Rehabilitacion Oral", case=False)))]
        # --------------------------------------------------------------------------------------------------------------------------------
        # Eliminar Periodoncia
        df_citas = df_citas.loc[~((df_citas["Nombre de la sede"].str.contains("Odontosanitas", case=False)) & 
                            (df_citas["Nombre de la especialidad / procedimiento"].str.contains("Periodoncia", case=False)))]
        # --------------------------------------------------------------------------------------------------------------------------------
        # Eliminar Odontologia General
        df_citas = df_citas.loc[~((df_citas["Nombre de la sede"].str.contains("Odontosanitas", case=False)) & 
                            (df_citas["Nombre de la especialidad / procedimiento"].str.contains("Odontologia General", case=False)))]
        # --------------------------------------------------------------------------------------------------------------------------------
        # Eliminar odontología general
        df_citas = df_citas.loc[~((df_citas["Nombre de la sede"].str.contains("Odontosanitas", case=False)) & 
                            (df_citas["Nombre de la especialidad / procedimiento"].str.contains("Odontologia General", case=False)))]
        # --------------------------------------------------------------------------------------------------------------------------------
        # Eliminar Endodoncia
        df_citas = df_citas.loc[~((df_citas["Nombre de la sede"].str.contains("Odontosanitas", case=False)) & 
                            (df_citas["Nombre de la especialidad / procedimiento"].str.contains("Endodoncia", case=False)))]
        # --------------------------------------------------------------------------------------------------------------------------------
        # Eliminar Cirugia Oral
        df_citas = df_citas.loc[~((df_citas["Nombre de la sede"].str.contains("Odontosanitas", case=False)) & 
                            (df_citas["Nombre de la especialidad / procedimiento"].str.contains("Cirugia Oral", case=False)))]
        # --------------------------------------------------------------------------------------------------------------------------------
        # Eliminar Odontologia Pediatrica
        df_citas = df_citas.loc[~((df_citas["Nombre de la sede"].str.contains("Odontosanitas", case=False)) & 
                            (df_citas["Nombre de la especialidad / procedimiento"].str.contains("Odontologia Pediatrica", case=False)))]
                

        # ruta guardar
        df_citas.to_excel(ruta_citas, index=False)
        #df_citas.to_excel(r'D:\MP68-Recordatorio de citas por Maria Maula\rta1.xlsx', index=False)
        return 2
    
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e)

print(Odontosanitas())

