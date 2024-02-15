import pandas as pd

df1 = pd.merge(fb_comments_count[(fb_comments_count['created_at'] >= '2019-12-01') & (
        fb_comments_count['created_at'] <= '2019-12-31')],
        fb_active_users, on='user_id', how='inner')
df2 = pd.merge(fb_comments_count[(fb_comments_count['created_at'] >= '2020-01-01') & (
        fb_comments_count['created_at'] <= '2020-01-31')],
        fb_active_users, on='user_id', how='inner')
result = pd.merge(df1.groupby('country')['number_of_comments'].sum(),
            df2.groupby('country')['number_of_comments'].sum(),
            on='country', suffixes=['_dec', '_jan'], how='outer')
result['rank_dec'] = result['number_of_comments_dec'].rank(method='dense', ascending=False)
result['rank_jan'] = result['number_of_comments_jan'].rank(method='dense', ascending=False)
result['rank_var'] = result['rank_jan'] - result['rank_dec']
list(result[(result['rank_var'] < 0) | (result.rank_dec.isnull())].index)