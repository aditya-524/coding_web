# Import your libraries
import pandas as pd

# Start writing code
employee_list.head()

#creating new dataframe and filtering last name and profession 
final_output = employee_list[(employee_list['last_name'] == 'Johnson') & (employee_list['profession'] == 'Doctor')]
#
final_output = final_output[['first_name', 'last_name']]
final_output