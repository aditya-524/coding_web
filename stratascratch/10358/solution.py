# Import your libraries
import pandas as pd

# Start writing code
user_purchases.head()

#created a new Dataframe for Friday and 1st Quarter
fri_firstq = (user_purchases[(user_purchases['day_name'] == "Friday") & (user_purchases['date'].dt.month <=3)])

#created a new column for week number
fri_firstq['week_number'] = fri_firstq['date'].dt.isocalendar().week

#created a dataframe with average spending per week
avg_friday = fri_firstq.groupby('week_number')['amount_spent'].mean().reset_index(name='mean_amount')

all_weeks = pd.DataFrame({'week_number': range(1, 14)})
final_output = all_weeks.merge(avg_friday, on='week_number', how='left')
final_output['mean_amount'] = final_output['mean_amount'].fillna(0)
final_output
