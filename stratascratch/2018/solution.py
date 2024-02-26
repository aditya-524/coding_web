# Import your libraries
import pandas as pd

# Start writing code
april_users = rc_calls[rc_calls['date'].dt.month==4]['user_id']
result = rc_users[(rc_users['status'] == 'free') & 
                  (~rc_users['user_id'].isin(april_users))]['user_id']