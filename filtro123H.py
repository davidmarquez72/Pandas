import sys
import pandas as pd

def filtros():
    try:
        # Ruta del archivo Excel original
        archivo_original = r"D:\MP74. Notificar Glosas Prestadores\04. Plantillas\REPORTE_DE_GLOSAS_BH_1.xlsx"

        # Ruta del archivo Excel donde se guardarán los registros filtrados
        archivo_filtrado = r"D:\MP74. Notificar Glosas Prestadores\04. Plantillas\REPORTE_DE_GLOSAS_BH_2.xlsx"

        # Leer el archivo Excel original en un DataFrame
        df_original = pd.read_excel(archivo_original)

        # cambiar de tipo a str la columna observacion
        df_original["OBSERVACIONES"] = df_original["OBSERVACIONES"].astype(str)

        # Filtrar los registros que no contengan "123H" ni "123h" en la columna "observacion"
        filtro = (~df_original["OBSERVACIONES"].str.contains("123H", na=False)) & (~df_original["OBSERVACIONES"].str.contains("123h", na=False))
        df_filtrado = df_original[filtro]

        # Guardar el DataFrame filtrado en un nuevo archivo Excel
        df_filtrado.to_excel(archivo_filtrado, index=False)
        return True
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        line_number = exc_traceback.tb_lineno
        e = f"Error en la linea {line_number}, {e}"
        return str(e)
    
