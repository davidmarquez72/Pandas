funtion noReporte()	

"Using the datetime library, I get the current date in the format ""yyyy-mm-dd"".
Using the os library, the dynamic path for the ""Do Not Report (Current Date).xlsx"" and ""REPORTE_DE_GLOSAS_BH.xlsx"" file is generated
The Pandas library is then used to read the files. Since the ""Do Not Report (Current Date).xlsx"" file is manually uploaded by a person in the area, the os library is used to verify its existence. If the file doesn't exist, the same information is taken from the ""REPORTE_DE_GLOSAS_BH.xlsx"" file and saved in a new file called ""REPORTE_DE_GLOSAS_BH_1.xlsx"".
If the file exists, the records found in ""Do Not Report (Current Date).xlsx"" are deleted from the ""REPORTE_DE_GLOSAS_BH.xlsx"" file. This is done using the merge function, where the records present in both files are identified and deleted from the first. To do this, the isin() function is used to check whether the values in the 'GLOSA ID' column of 'dfrepgen' are present in the 'GLOSA ID' column of 'crossover'. The ~ operator is used to reverse the result, i.e. select all rows in 'dfrepgen' where the 'GLOSA ID' is not present in 'junction'.
Finally, the function returns a value of 2 if executed successfully. Otherwise, it returns the error line along with an explanatory message of the error."

librarys: sys, pandas, datetime, os
