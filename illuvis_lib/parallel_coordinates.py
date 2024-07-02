import plotly.express as px

def create_custom_parallel_coordinates(data, dimensions, color_col, chart_title='Custom Parallel Coordinates'):
    """
    Creates a custom parallel coordinates plot using Plotly.

    Parameters:
    - data: DataFrame containing the data.
    - dimensions: List of columns to be used as dimensions.
    - color_col: Column to be used for coloring lines.
    - chart_title: Title of the chart.
    
    Returns:
    - None
    """
    # Map categorical color_col to numeric values
    if data[color_col].dtype == object:
        unique_values = data[color_col].unique()
        color_map = {val: idx for idx, val in enumerate(unique_values)}
        data[color_col] = data[color_col].map(color_map)

    fig = px.parallel_coordinates(data, dimensions=dimensions, color=color_col, title=chart_title)
    fig.show()
