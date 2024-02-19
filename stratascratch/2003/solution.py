# Import your libraries
import pandas as pd

# Start writing code
loans.head()
# submissions.head()

result = loans.loc[
    loans[loans["type"] == "Refinance"]
    .groupby("user_id")["created_at"]
    .idxmax()
]
result = pd.merge(result, submissions, left_on="id", right_on="loan_id", how="left")
result = result[["user_id", "balance"]]

result