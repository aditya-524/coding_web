# Import your libraries
import pandas as pd

# Start writing code
rc_calls.head()
df = rc_calls.groupby('user_id')['date'].count().to_frame('n_calls').reset_index()
df = pd.merge(df, rc_users[['user_id', 'company_id']], on='user_id')
df['rank'] = df.groupby('company_id')['n_calls'].rank('dense', ascending = False)
result = df[df['rank'] <= 2].sort_values(by=['company_id', 'rank'])[['company_id', 'user_id', 'rank']]