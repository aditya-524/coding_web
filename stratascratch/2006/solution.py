# Import your libraries
import pandas as pd

# Start writing code
facebook_posts.head()


facebook_posts.groupby(facebook_posts.post_date.dt.day).size().reset_index()