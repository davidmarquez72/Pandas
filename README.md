funtion macrodias()

"Using the datetime library, I get the current date in the format ""yyyy-mm-dd"".
Using the os library, the dynamic path for the ""Pendientes2.xlsx"" and ""Festivos.xlsx"" file is generated
Then, using the Pandas library, the files are read and the dates are reformatted to 'dd/mm/yyyy'. First, this change is applied in the 'HOLIDAYS' column of the ""Festivos.xlsx"" file and then in the 'Date of Issue' column of the ""Pendientes2.xlsx"" file, using the 'to_datetime' function of Pandas.
A list of dates from the ""Festivos.xlsx"" file is then created. Next, a function is defined within the 'calcular_dias_laborables' function, which is designed to determine the number of working days between two dates, excluding the holidays provided in the 'festivos_list' list. This function uses a 'while' loop to iterate over each day between 'fecha_inicio' and 'fecha_fin'. In each iteration, check to see if the day of the week of the current date is a working day (Monday through Friday) and if the date is not present in the holiday list. If both conditions are met, the 'dias_laborables' counter is incremented. In the end, the function returns the total number of working days found.
Subsequently, Pandas' 'apply' function is used to apply a custom function to each row in the 'df_pend3' DataFrame. The custom function is specified by a lambda expression that takes the current row of the DataFrame as input and calculates the working days between the date of shipment of that row (column ""Date Shipped"") and a given current date, using the 'calcular_dias_laborables' function. The result of this operation is assigned to a new column named ""Days"" in the 'df_pend3' DataFrame.
Finally, the DataFrame is sorted by 'Authorization Number' and the result is saved in an Excel file called ""Pendientes3.xlsx"".
Finally, the function returns a value of 2 if executed successfully. Otherwise, it returns the error line along with an explanatory message of the error."


funtion diasAntiguedad()	


"Using the datetime library, I get the current date in the format ""yyyy-mm-dd"".
A path for the pending file (""Pendientes3.xlsx"") is dynamically generated using the current date. The path is constructed by combining the current date with the base path where the output files will be saved.
A path is defined for the holiday file (""Festivos.xlsx""). The ""festivos.xlsx"" file containing the holiday dates is read into another DataFrame named 'df_festivos'.
A function called 'asignar_antiguedad' is created that assigns a seniority tag based on the number of days. If the number of days is greater than 50, the label ""Greater than 50 days"" is assigned. If the number of days matches an entry in the 'DAYS' column of the Holiday DataFrame, the corresponding value is assigned to the 'DAYS OLD' column. If there are no matches, 'None' is returned.
The 'asignar_antiguedad' function is applied to the ""Days"" column of the 'df_pend3' DataFrame, resulting from the reading of the pending file. The result is stored in a new column called ""Days Old.""
Finally, the DataFrame 'df_pend3' with the new ""Days Old"" column is saved in the ""Pendientes3.xlsx"" file using the same dynamic path defined above,
Finally, the function returns a value of 2 if executed successfully. Otherwise, it returns the error line along with an explanatory message of the error."


funtion oportunidad()	

"Using the datetime library, I get the current date in the format ""yyyy-mm-dd"".
The path of (""Pendientes3.xlsx"") is reused and read into a DataFrame, checking for the following business rules: 
if the value in the ""Plan Description"" column is ""COLSANITAS DENTAL PLAN"" and if the number of days in the ""Days"" column is less than or equal to 2. In such a case, it returns ""TIMELY"".
If the ""PENDING/MEETINGS/AHC"" column has the value ""AHC"", it returns ""TIMELY"" if the number of days in the ""Days"" column is greater than 3, otherwise, it returns ""TIMELY"".
If the ""PENDING/MEETINGS/AHC"" column has the value ""MEETINGS"", it returns ""INOPPORTUNE"" if the number of days in the ""Days"" column is greater than or equal to 11, otherwise, it returns ""TIMELY"".
If the ""PENDING/BOARDING/AHC"" column has the value ""PENDING"", it returns ""UNTIMELY"" if the number of days in the ""Days"" column is greater than 1, otherwise, it returns ""TIMELY"".
In any other case, return 'None'. This function is then applied to the relevant columns of the 'df_pend3' DataFrame using the 'apply' method. The result is stored in a new column called ""Opportunity"". Finally, the resulting DataFrame is saved to a CSV file in the path specified by 'ruta_pendtxt'.
Finally, the function returns a value of 2 if executed successfully. Otherwise, it returns the error line along with an explanatory message of the error."

libraries:sys, pandas, datetime, os, openpyxl
