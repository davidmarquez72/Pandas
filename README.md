funtion duplicados()

"Using the datetime library, I get the current date in the format ""yyyy-mm-dd"".
The Pandas library is used to read the ""Union.xlsx"" file. The duplicate GLOSA IDs are then searched using the .duplicated function in the 'GLOSA ID' column, and stored in a new DataFrame. This new DataFrame is checked to see if it contains information; if yes, it is saved in an Excel file. If it contains no information, a message is printed.
Finally, the function returns a value of 2 if executed successfully. Otherwise, it returns the error line along with an explanatory message of the error."


funtion filtro(strDateSpecific)	

"Using the datetime library, I get the current date in the format ""yyyy-mm-dd"".
The Pandas library is used to read the ""Union.xlsx"" file. All records containing ""COLSANITAS"" or ""MEDISANITAS"" are then selected in the 'PRODUCT' column using the .str.contains function. Records that have the status 'SENT TO TREASURY' in the 'STATUS' column are then filtered using the .str.contains function. Subsequently, the records with the current date are selected in the 'POSTED DATE' column using the .str.contains function. The results are overwritten in the original Excel file.
The Excel file is then uploaded using the load_workbook function of the openpyxl library. The name of the sheet is renamed from ""Sheet1"" to ""Sheet1"" and the file is saved.
This feature is designed so that if a specific date is received, it is selected in the 'POSTING DATE' filter, following the same process described above.
Finally, the function returns a value of 2 if executed successfully. Otherwise, it returns the error line along with an explanatory message of the error.
"

libraries: sys, pandas, datetime, os, openpyxl

