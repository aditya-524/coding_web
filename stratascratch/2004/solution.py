# Import your libraries
import pandas as pd
from datetime import datetime, timedelta

# Start writing code
start_date = pd.to_datetime('2020-02-10') - pd.DateOffset(days=30)
end_date = '2020-02-10'
result = fb_comments_count.loc[fb_comments_count['created_at']
    .between(start_date, end_date)] \
    .groupby('user_id', as_index=False) \
    ['number_of_comments'].sum()

result 
