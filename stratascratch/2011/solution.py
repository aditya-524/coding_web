# Import your libraries
import pandas as pd

# Start writing code
twitch_sessions.head()

alpha =twitch_sessions.copy()
alpha['duration'] = alpha['session_end'] - alpha['session_start']

# alpha.head()
beta = alpha.pivot_table(index='session_type', values='duration', aggfunc = "mean" ).reset_index()
beta
