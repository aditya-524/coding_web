# Import your libraries
import pandas as pd

# Start writing code
# Import your libraries
import pandas as pd
import numpy as np

# Start writing code
df = da_flights.copy()

df = pd.merge(pd.merge(df, df, left_on='destination', right_on='origin', how='left'), df, left_on='destination_y', right_on='origin', how='left')




df['cost0'] = df['cost_x']
df['cost1'] = df['cost_x'] + df['cost_y']
df['cost2'] = df['cost_x'] + df['cost_y'] + df['cost']

df['dest0'] = df['destination_x']
df['dest1'] = df['destination_y']
df['dest2'] = df['destination']


df2 = pd.concat([pd.DataFrame(df[['origin_x','dest0', 'cost0']].values),
pd.DataFrame(df[['origin_x','dest1', 'cost1']].values),
pd.DataFrame(df[['origin_x','dest2', 'cost2']].values)])

df2.groupby([0, 1])[2].min().reset_index()
