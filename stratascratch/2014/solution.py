# Import your libraries
import pandas as pd

# Start writing code
postmates_orders.head()
alpha = postmates_orders[['customer_id', 'order_timestamp_utc']]
alpha['hour']  = alpha.order_timestamp_utc.dt.hour
alpha['day']  = alpha.order_timestamp_utc.dt.date

beta = alpha.groupby(["day", "hour"]).size()\
            .to_frame("n_orders")\
            .groupby("hour")["n_orders"].mean()\
            .reset_index()\
            .nlargest(n=1, columns="n_orders", keep="all")
beta