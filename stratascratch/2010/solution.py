# Import your libraries
import pandas as pd

# Start writing code
twitch_sessions.head()
df = twitch_sessions.copy()
df = df.pivot_table(index = 'user_id', columns = "session_type", values = "session_id", aggfunc = "count").reset_index()
df = df.rename(columns = {"streamer": "streaming_num", "viewer": "viewer_num"})
df = df.query('streaming_num > viewer_num')
df