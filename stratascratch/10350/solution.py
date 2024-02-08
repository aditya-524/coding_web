# Import your libraries
import pandas as pd

# Start writing code
fb_search_events.head()

# print(fb_search_events["search_id"].value_counts())
#so all search_id are not unique

#creating a copy of the dataframe
df = fb_search_events.copy()

# dropping the column which is irrelavant
df = df.drop('search_term', axis=1)

for index, row in df.iterrows():
    if row['clicked'] == 0:
        df.loc[index, 'ratings'] = 1
    elif row['search_results_position'] > 3:
        df.loc[index, 'ratings'] = 2
    else:
        df.loc[index, 'ratings'] = 3
        
df_final = df.sort_values(['search_id', 'ratings'],ascending=[True, False]).drop_duplicates('search_id', keep='first')
                            

df_final.drop(['clicked', 'search_results_position'], axis=1, inplace=True)
df_final
