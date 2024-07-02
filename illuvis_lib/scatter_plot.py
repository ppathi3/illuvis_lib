import plotly.express as px
import pandas as pd

def create_custom_scatter_plot(data, x_col, y_col, color_col=None, chart_title='Custom Scatter Plot', x_title='X-Axis', y_title='Y-Axis'):
    """
    This function creates a custom scatter plot using the Plotly library with customizable options.

    Parameters:
    data (DataFrame): A pandas DataFrame containing the data.
    x_col (str): The column name for the x-axis values.
    y_col (str): The column name for the y-axis values.
    color_col (str, optional): The column name for color grouping. If None, no grouping is applied.
    chart_title (str, optional): Title for the chart.
    x_title (str, optional): Title for the x-axis.
    y_title (str, optional): Title for the y-axis.

    Returns:
    None. The function displays the scatter plot using Plotly's show() method.
    """
    # Ensure color_col is treated as a categorical variable if it's not numeric
    if color_col and not pd.api.types.is_numeric_dtype(data[color_col]):
        data[color_col] = data[color_col].astype(str)

    fig = px.scatter(data, x=x_col, y=y_col, color=color_col, title=chart_title)
    fig.update_layout(
        xaxis_title=x_title,
        yaxis_title=y_title
    )
    
    fig.show()
