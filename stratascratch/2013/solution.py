# Import your libraries
import pandas as pd

# Start writing code
postmates_orders.head()

postmates_orders.agg(func={'customer_id':'nunique', 'amount':'mean'})