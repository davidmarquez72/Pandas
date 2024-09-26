funtion Quitar57()	

"A dynamic path is constructed for the archiving of face-to-face medical appointments using the current date. The path is created using the os.path.join function to ensure portability between different operating systems.
The Excel file of face-to-face medical appointments is loaded into a Pandas DataFrame using the pd.read_excel function.
A function called eliminar_57 is defined, which receives a number as input. This function converts the number into a string and checks if the first two digits are '57'. If so, remove these two digits and return the number as an integer. If the number does not start with '57', it is returned unchanged.
The eliminar_57 function is applied to the 'Phone 1' and 'Phone 2' columns of the DataFrame using Pandas' apply method. This removes the '57' prefix from phone numbers in these columns, where applicable.
Finally, the function returns a value of 2 if executed successfully. Otherwise, it returns the error line along with an explanatory message of the error."	

libraries: sys, pandas, datetime, os, openpyxl
