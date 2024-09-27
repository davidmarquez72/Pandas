funtion erroresCol()	

"The paths of the input and output files are defined. 'archivo_original' contains the path of the original CSV file to be processed, while 'archivo_errores' contains the path where the file containing the failed lines will be saved.
Two empty lists are created: 'lineas_correctas' to store the lines in the original file that have the correct number of fields, and 'lineas_errores' to store the lines that have the wrong number of fields.
An attempt is made to open the original file in read mode ('r') using a 'try-except' block to handle possible file opening errors. Each line of the file is cycled using a 'for' loop. Each line is divided into fields using the '|' separator and checked if the number of fields is equal to 59. If so, the line is added to the 'lineas_correctas' list; otherwise, 'lineas_errores' is added to the list.
The contents of the 'lineas_errores' list are saved in a separate file using a 'with open' block in write mode ('w'). This ensures that the file closes properly after the lines are typed.
The correct lines are converted into a DataFrame using a list understanding and the 'pd. DataFrame'. Each line is again split into fields using the '|' separator and a row is created in the DataFrame for each line. This resulting DataFrame, called a 'frame', will contain all the lines in the original file that have the correct number of fields.
Finally, the function returns a value of 2 if executed successfully. Otherwise, it returns the error line along with an explanatory message of the error."


funtion erroresMed()	


"the same function ded errorCol() is repeated, only now it is executed relative to the MEDISANIAS.txt file and the errors are saved in erroresMEDISANTIAS.txt
Finally, the function returns a value of 2 if executed successfully. Otherwise, it returns the error line along with an explanatory message of the error."


funtion union():	

"Two text files separated by '|', containing data from COLSANITAS and MEDISANITAS, respectively, are read. The data is stored in two DataFrames, 'frame' and 'frame2', using Pandas' 'pd.read_csv' function. The '|' separator is specified and all columns in the file are included using the 'usecols=range(0, 59)' parameter. 'low_memory=False' is used to avoid memory-related warnings.
It combines the two DataFrames into a single one called 'frame_final' using Pandas' '_append' method. This vertically joins the two DataFrames.
The combined DataFrame 'frame_final' is converted to an Excel file using Pandas' 'to_excel' method. The file is saved in the specified path with the name (""Union.xlsx"") with the sheet name 'Sheet1' and without including the row index in the Excel file ('index=None' parameter).
Finally, the function returns a value of 2 if executed successfully. Otherwise, it returns the error line along with an explanatory message of the error."

libraires: sys, pandas
