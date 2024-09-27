funtion QuitarCaracteres()	


"The current date is obtained in the format 'YYYY-MM-DD' using the datetime library and the strftime method.
The dynamic path for the base Excel file is constructed using the current date. The path is created using the os.path.join function to ensure portability between different operating systems.
The Excel file is loaded into a Pandas DataFrame using the pd.read_excel function.
The unidecode function is applied to all cells in the DataFrame to remove accents from special characters.
Double and single quotes throughout the DataFrame are replaced with empty strings using the replace method with a regular expression.
The columns 'Phone 1', 'Phone 2', 'Site Code' and 'Patient Document Number' are converted to string data type and the '.0' at the end of the numbers are removed using the str.replace method. The file is then loaded by the load_workbook function and the sheet is renamed 
The modified DataFrame is saved in the same Excel file by overwriting the original, using the Pandas to_excel method with the index=False parameter.
Finally, the function returns a value of 2 if executed successfully. Otherwise, it returns the error line along with an explanatory message of the error."	

libraries: sys, pandas, datetime, os, openpyxl, unicode
