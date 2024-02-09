# Import your libraries
import pandas as pd

# Start writing code
marketing_campaign.head()

df = marketing_campaign.copy()
df = marketing_campaign
df1 = df.groupby('user_id').created_at.min().reset_index()
df2 = df.groupby(['user_id', 'product_id']).created_at.min().reset_index()
df3 = pd.merge(df1, df2, on = 'user_id')
df4 = df3.query('created_at_x != created_at_y')
df4.user_id.drop_duplicates().size