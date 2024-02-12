# Import your libraries
import pandas as pd

# Start writing code
submissions.head()
df = submissions[['loan_id', 'balance', 'rate_type']]
df['total'] = df.groupby('rate_type')['balance'].transform(sum)
df['percent'] = df['balance']/df['total']
df[['loan_id', 'rate_type', 'balance', 'percent']]
df['balance_share'] = df['percent']*100
df.drop(['percent','total'], inplace=True, axis=1)
df