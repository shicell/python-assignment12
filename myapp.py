""" Task 4: A Dashboard with Dash """

from dash import Dash, dcc, html, Input, Output # Dash components you need
import plotly.express as px # Dash relies on Plotly to actually do the plotting.  Plotly creates an HTML page with lots of JavaScript.
import plotly.data as pldata # This is only needed to give access to the Plotly built in datasets.

# 1.1 load gapminder dataset
df = pldata.gapminder(return_type='pandas') # This loads one of the datasets
print(df.head(5))

# 1.2 create series of unique country names
countries = df['country'].unique()
print(countries)

# Initialize Dash app
app = Dash(__name__)
server = app.server

app.layout = html.Div([
    dcc.Dropdown(
        id="country-dropdown",
        options=[{"label": country, "value": country} for country in countries],
        value="Canada"
    ),
    dcc.Graph(id="gdp-growth")
])

# Callback for dynamic updates
@app.callback( 
    Output("gdp-growth", "figure"),
    [Input("country-dropdown", "value")]
)
def update_graph(country):
    fig = px.line(df[df["country"]==country], x="year", y="gdpPercap"
                  , title=f"{country} GDP Per Capital over Time")
    return fig

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
