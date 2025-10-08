""" Task 3: Interactive Visualizations with Plotly """

import plotly.express as px
import plotly.data as pldata
import numpy as np

# 3.1 Load Plotly wind dataset and print first 10 and last 10 lines
df = pldata.wind(return_type='pandas')
print(df.head(10))
print(df.tail(10))

# 3.2 convert the 'strength' column to a float (gathering average of each range)
df['all_strengths'] = df['strength'].str.findall(r'\d+')
df['all_strengths'] = df['all_strengths'].apply(lambda x: [float(item) for item in x])
df['strength'] = df['all_strengths'].apply(np.mean)

# 3.3 create interactive scatter plot of strength vs. frequency, with colors based on the direction
fig = px.scatter(df, x='strength', y='frequency', color='direction',
                 title="Wind Data, Strength vs. Frequency", hover_data=["frequency"])

# 3.4 save and load the HTML file, as wind.html
fig.write_html("wind.html", auto_open=True)
