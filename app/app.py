import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import datetime

CLOCK_COLOR = os.environ.get("CLOCK_COLOR", "#ffd43b")

app = dash.Dash(__name__)

app.layout = html.Div(
    style={
        "display": "flex", "flexDirection": "column", "alignItems": "center", "justifyContent": "center",
        "height": "100vh", "background": "linear-gradient(135deg, #222, #228be6 85%)"
    },
    children=[
        html.H1("Theo dõi đồng hồ từ Raspberry Pi ở tầng Device", style={"fontSize": "80px", "color": "#fff", "marginBottom": "150px", "textAlign": "center"}),
        html.Div(id="clock", style={
            "fontSize": "150px", "fontFamily": "monospace", "color": CLOCK_COLOR,
            "padding": "25px 60px", "borderRadius": "30px", "background": "rgba(0,0,0,0.4)",
            "boxShadow": "0 4px 32px 0 rgba(34,139,230,0.25)"
        }),
        dcc.Interval(id="interval", interval=1000, n_intervals=0)
    ]
)

@app.callback(
    Output("clock", "children"),
    Input("interval", "n_intervals")
)
def update_clock(n):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    return now

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050, debug=False)