# src/app/main.py
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# Sample data
df = pd.DataFrame({"x": [1, 2, 3, 4, 5], "y": [10, 20, 25, 30, 35]})
fig = px.line(df, x="x", y="y", title="Dynamic Data Plot")

# Create app
app = Dash(__name__)
app.layout = html.Div([
    html.H1("My Dynamic Website"),
    dcc.Graph(figure=fig)
])

# Define main function
def main():
    app.run(debug=True, host='0.0.0.0')

# Run the app if executed directly
if __name__ == "__main__":
    main()
