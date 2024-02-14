# Import your libraries
import pandas as pd

# Start writing code
fb_active_users.head()


result = fb_active_users[fb_active_users['country'] == 'USA'].groupby('status')['user_id'].count().to_frame('user_count')
result = result.loc['open'] / result['user_count'].sum()
