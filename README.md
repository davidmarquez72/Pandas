funtion Centros()

"Using the datetime library, I get the current date in the format ""yyyy-mm-dd"".
By means of the os library, the dynamic path for the gloss report is generated, since the file generated on the day is taken.
With the help of Pandas, I read the files 'PROVIDER CENTERS MEDICOS_GLOSAS.xlsx' and 'Report Glosas.xlsx'. Using the merge function, I cross-reference data where the 'MEDICAL ID' is identified in the df_centros_medicos DataFrame and the 'PROVIDER IDENTIFICATION NUMBER' in the df_reporte DataFrame, selecting all the records that match. Subsequently, it is validated if the DataFrame created after the crossing is empty. If yes, a message is displayed; otherwise, an Excel file called 'Report of Glosses Providers Medical Centers {current_date}.xlsx' is generated, where {current_date} represents the current date and returned a 2 if the function was executed correctly, otherwise it returns the line of error and error."

librarys: sys, pandas, datetime, os

