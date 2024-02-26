# Import your libraries
import pandas as pd

# Start writing code
# rc_calls.head()
# rc_users.head()
alpha = pd.merge(rc_calls, rc_users, on = "user_id", how='left')
alpha.head()
beta = alpha\
        [(alpha['status'] == 'paid') &
        (alpha['date'].dt.month == 4) & 
        (alpha['date'].dt.year == 2020)]
final = beta['user_id'].nunique()
                
final