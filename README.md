funtion asignacion()	

"The current date is obtained in day-month-year format using the strftime function of the datetime library.
A dynamic path is created for the pending file from the current date.
The text file is loaded into a Pandas DataFrame (df_pendientes) using the pd.read_csv function, specifying the '|' separator and the 'latin-1' encoding.
A series of corresponding conditions and values are defined to assign a new column called 'Event Number' based on the values in the 'Observation Code' column.
The DataFrame is sorted by the 'Authorization Number' column in ascending order.
A new DataFrame called df_Pendientes_OrdenEvento is created that contains only the unique rows based on the 'Authorization Number' and is sorted by 'Event Number'.
A new DataFrame named df_pendientes_Nivel is created that contains only the 'Authorization Number' and 'Authorization Level' columns.
A new DataFrame called df_Pendientes_OrdeNivel is created that contains only the unique rows according to the 'Authorization Number' and is sorted by 'Authorization Level'.
An INNER JOIN operation is performed between the df_Pendientes_OrdenEvento and df_Pendientes_OrdeNivel DataFrames using the 'Authorization Number' column.
The 'Autorización_y Level' column is renamed to 'Authorization Level' and the unnecessary columns are removed.
A new dynamic path is created for the output file 'Pendientes.xlsx'.
The resulting DataFrame is saved to an Excel file using the to_excel function.
Finally, the function returns a value of 2 if executed successfully. Otherwise, it returns the error line along with an explanatory message of the error."	

libraries: sys, pandas, datetime, os, openpyxl, numpy

