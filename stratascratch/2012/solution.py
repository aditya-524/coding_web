# Import your libraries
import pandas as pd

# Start writing code
twitch_sessions.head()

alpha = twitch_sessions.sort_values('session_start')\
                .groupby('user_id')\
                .filter(lambda x: x['session_type'].iloc[0]=='viewer')\
                .pivot_table(index='user_id', columns='session_type', 
                            values = 'session_id', aggfunc='count')\
                .reset_index()\
                .drop(columns='viewer')
                    
alpha = alpha.rename(columns={'streamer': 'n_sessions'})                
                    