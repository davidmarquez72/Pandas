funtion copy()

"Using the datetime library, I get the current date in the format ""yyyy-mm-dd""
Using the os library, I generate a dynamic path of the informacion.xlsx file and the Report template Glosas.xlsx
By means of Pandas I read the files, then select only the columns that are necessary from the Info file and then write the template with the selected columns.
using the openpyxl library I change the name of the sheet from 'Sheet1' to 'Sheet1' and return a 2 if the function was executed successfully, otherwise it returns the error line and the error.
"

librarys: sys, pandas, datetime, os, openpyxl
