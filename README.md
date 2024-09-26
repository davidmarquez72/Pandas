funtion separar()	

"The current date is obtained in the format 'YYYY-MM-DD' using the datetime library and the strftime method.
A dynamic path is created for the gloss report file using the current date. The path is constructed using the os.path.join function to ensure portability between different operating systems.
The gloss report Excel file is loaded into a Pandas DataFrame using the pd.read_excel function.
A dictionary called 'dfs_dict' is created to store DataFrames separated by the provider's identification number. It iterates over the unique values of the 'PROVIDER IDENTIFICATION NUMBER' column in the 'df' DataFrame. For each unique value, the original DataFrame is filtered to obtain a DataFrame that contains only the rows corresponding to that ID number and is added to the dictionary with the ID number as the key.
It is iterated over the 'dfs_dict' dictionary and each DataFrame is written in a separate Excel file. For each key-value pair in the dictionary, a unique file name is created using the lender identification number and the current date. The to_excel method is then used to write the DataFrame to the corresponding Excel file. The index=False parameter is used to prevent the row index from being added to the Excel file.
Finally, the function returns a value of 2 if executed successfully. Otherwise, it returns the error line along with an explanatory message of the error."	

libraries: sys, pandas, datetime, os
