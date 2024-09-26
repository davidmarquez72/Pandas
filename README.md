funtion divyvencer()	

"Using the datetime library, I get the current date in the format ""yyyy-mm-dd"".
Using the os library, the path for the ""Archivo_Plano_EPS.txt"" file is dynamically generated. The maximum allowed size in bytes (1GB) is stored in a variable. Using the os.path.getsize function, the file size ""Archivo_Plano_EPS.txt"" is obtained. It is validated if the file size exceeds the set limit.
If the file size exceeds the limit, proceed as follows:
The original file opens in read mode with Latin-1 encoding.
It iterates over each line of the file.
If it's the first line, it's saved as the header.
The current line is added to the current segment and validated if the segment size exceeds the maximum allowed size.
If the size of the segment exceeds the limit, the segment is saved to a new file.
The header and data are written to the split file.
The current segment and size is reset, and this process is repeated until all the necessary files are created.
Finally, if there is any data remaining in the last segment, it is saved in an additional file.
Finally, the function returns a value of 2 if executed successfully. Otherwise, it returns the error line along with an explanatory message of the error."	

libraries: sys, datetime, os

