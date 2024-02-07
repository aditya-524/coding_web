# Import your libraries
import pandas as pd

# Start writing code
employee_list.head()
employee_list

prior_output = employee_list[['profession','birth_month']]


final_output = prior_output.pivot_table(index='profession', columns='birth_month', aggfunc='size', fill_value=0)
final_output.columns = [f'Month_{i}' for i in range(1, 13)]
final_output.index.name = 'department'
final_output.reset_index(inplace=True)

final_output
