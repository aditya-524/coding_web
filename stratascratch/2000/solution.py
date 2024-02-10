# Import your libraries
import pandas as pd

# Start writing code
submissions.head()

#create a different dataframe
alpha = submissions.copy()
# alpha = alpha[["loan_id", "rate_type"]]
# Use pivot tables
output = alpha.pivot_table(index='loan_id', columns='rate_type',aggfunc='size',fill_value=0)

# finalizing the structure
output.index.name = 'loan_id'
output.reset_index(inplace=True)
output