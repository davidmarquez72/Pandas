clinicaDental(): 


"Using the datetime library, I get the current date in the format ""yyyy-mm-dd"" and the next day's date. 
With the os library, I generate a dynamic path that includes the date of the day and the name of the file that contains the date of the next day. 
I use the pandas library to read the file and convert it into a DataFrame. Subsequently, I delete records that have 'Dental Clinic' in the 'Location Name' column and 'Maxillary Orthopedics' in the 'Specialty/Procedure Name' column. I repeat this process by removing the following specialties from the ""Name of Specialty/Procedure"" column: ""Orthodontics"", ""Oral Rehabilitation"", ""Periodontics"", ""General Dentistry"", ""Endodontics"", ""Oral Surgery"" and ""Pediatric Dentistry"". Finally, I overwrite the same file and return a 2 if the function was executed successfully, otherwise it returns the error and error line."

Odontosanitas():

"Using the datetime library, I get the current date in the format ""yyyy-mm-dd"" and the next day's date. 
With the os library, I generate a dynamic path that includes the date of the day and the name of the file that contains the date of the next day. 
I use the pandas library to read the file and convert it into a DataFrame. Subsequently, I delete records that have 'Odontosanitas' in the 'Site Name' column and 'maxillary orthopedics' in the 'Specialty/Procedure Name' column. I repeat this process by removing the following specialties from the ""Name of Specialty/Procedure"" column: ""Orthodontics"", ""Oral Rehabilitation"", ""Periodontics"", ""General Dentistry"", ""Endodontics"", ""Oral Surgery"" and ""Pediatric Dentistry"". Finally, I overwrite the same file and return a 2 if the function was executed successfully, otherwise it returns the error and error line."

librarys using: sys, pandas, datetime, os


