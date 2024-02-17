# Import your libraries
import pandas as pd

# Start writing code
twitch_sessions.head()


result = twitch_sessions.groupby('user_id')['session_type'].nunique().to_frame('n_types').reset_index()
result = result[result['n_types'] == 2]['user_id']
