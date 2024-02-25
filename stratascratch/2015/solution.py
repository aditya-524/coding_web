# Import your libraries
import pandas as pd

# Start writing code
postmates_orders.head()
# date_a = '2019-03-11'
# date_b = '2019-04-11'
# postmates_markets.head()
# alpha = pd.merge(postmates_orders[
#                 (postmates_orders['order_timestamp_utc']>='2019-03-11') &
#                 (postmates_orders['order_timestamp_utc']<='2019-04-11')],
#                 postmates_markets, left_on='city_id', right_on='id', how='inner' )
# alpha.head()        
# result = alpha.loc[alpha['order_timestamp_utc']
#         .between(date_a, date_b)]\

result = postmates_orders.groupby([postmates_orders['order_timestamp_utc'
                        ].dt.date, postmates_orders['city_id'
                        ]])['amount'].sum().unstack(level=0)
result['amount_difference'] = result.iloc[:, 1] - result.iloc[:, 0]
result = result[(result['amount_difference'] == result['amount_difference'].min())
            | (result['amount_difference'] == result['amount_difference'
            ].max())]['amount_difference'].reset_index()
result = pd.merge(result, postmates_markets, left_on='city_id',
            right_on='id')[['name', 'amount_difference']]
      