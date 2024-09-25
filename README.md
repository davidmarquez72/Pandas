funtion cruceCodigo()

"Using the datetime library, I get the current date in the format ""yyyy-mm-dd"" and the next day's date. 
Through the bookstore, the dynamic route for Face-to-Face Medical Appointments is generated.
The file ""Face-to-Face Medical Appointments"" and the file ""Codes.xslx"" are read using the pandas library. Then, the merge function is used to perform a data cross-reference where the codes that are the same are identified in the 'Resource Code' column. If matching records are found, they are saved in an Excel file.
Subsequently, the isin() function is used to verify that the ""In-Person Medical Appointments"" codes are present in ""Codes"". Using the '~' operator, the selection is reversed to identify all codes that are not present. Then, the ""Face-to-Face Medical Appointments"" file is overwritten, thus eliminating codes that should not be used.
The function returns a value of 2 if executed successfully. Otherwise, it returns the error line along with the corresponding error message."	

librarys: sys, pandas, datetime, os

