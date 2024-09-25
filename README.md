funtion CrucePlanoEps()	

"Using the datetime library, I get the current date in the format ""yyyy-mm-dd"".
Through the library, the dynamic route for Pendientes_Archivo_EPS.txt and Archivo_Plano_EPS.txt is generated.
The Pandas library is used to read text files, specifying that the separator is '|' and that the encoding is 'Latin-1'. Records containing ""SI"" are then selected in the ""shared users"" column of the drawing, and prefixed to the resulting DataFrame, naming it df_siplano.
Subsequently, a cross-check is made in the ""Authorization number"" column between the selected ""SI"" and EPS records. Only the ""Pendientes_Archivo_EPS"" columns are retained, and the DataFrame is saved in a text file with '|' separator and 'Latin-1' encoding.
The function returns a value of 2 if executed successfully. Otherwise, it returns the error line along with the corresponding error message."	


funtion cruceLista()	

"Using the datetime library, I get the current date in the format ""yyyy-mm-dd"".
Using the os library, the dynamic path for the 'cruce_EPS.txt' and 'BRANCH MP.xlsx' files is generated. The pandas library is then used to read both files. Subsequently, records are filtered into 'BRANCH MP.xlsx' that contain 'YES' in the 'shared users' column and that also have the value 'x' in the 'To assign' column.
Pandas' merge function is used to combine the 'df_cruceEps' and 'df_listselec' DataFrames, based on the matching of the values in the 'Filing Branch' column in 'df_cruceEps' and 'Branch' in 'df_listselec'. Only rows that have matches in both tables will be included.
The function returns a value of 2 if executed successfully. Otherwise, it returns the error line along with an explanatory message of the error."	

librarys: sys, pandas, datetime, os
