funtion filtros()	

"Defines the path of the original Excel file and the path where the filtered records will be saved.
Use the Pandas library to read the original Excel file and load it into a DataFrame called 'df_original'.
Change the data type in the 'OBSERVATIONS' column to a text string (str) using the 'astype' method.
Filter out records that don't contain the string ""123H"" or ""123h"" in the ""OBSERVATIONS"" column. This is achieved by creating a Boolean filter that selects rows where the 'OBSERVATIONS' column does not contain any of these strings, using the 'str.contains' function.
The filter is applied to the 'df_original' DataFrame, resulting in a new DataFrame named 'df_filtrado' that contains only the records that meet the filter.
Finally, the filtered DataFrame is saved in a new Excel file at the path specified by 'archivo_filtrado', using Pandas' 'to_excel' method. The 'index=False' parameter indicates that the DataFrame indexes will not be included in the resulting Excel file.
Finally, the function returns a value of 2 if executed successfully. Otherwise, it returns the error line along with an explanatory message of the error."	

libraies: sys, pandas
