import plotly.graph_objects as go

def create_custom_bar_chart(data, colors=None, x_label='Categories', y_label='Values', legend_title='Legend', chart_title='Custom Bar Chart'):
    """
    This function creates a custom bar chart using Plotly library with customizable options.

    Parameters:
    data (dict): A dictionary where keys are categories and values are corresponding values.
    colors (list, optional): List of colors for each bar in the chart. If None, default colors are used.
    x_label (str, optional): Label for the x-axis.
    y_label (str, optional): Label for the y-axis.
    legend_title (str, optional): Title for the legend.
    chart_title (str, optional): Title for the chart.

    Returns:
    None. The function displays the bar chart using Plotly's show() method.

    Example:
    >>> data = {'Category1': 10, 'Category2': 20, 'Category3': 30}
    >>> colors = ['blue', 'green', 'orange']
    >>> create_custom_bar_chart(data, colors=colors, x_label='X Axis Label', y_label='Y Axis Label', legend_title='My Legend', chart_title='My Custom Chart')
    """

    labels = list(data.keys())
    values = list(data.values())
    
    # Use default colors if not provided by user
    if colors is None:
        colors = ['blue', 'green', 'orange', 'red', 'purple']  # Default colors
    
    # Create a trace for each bar with specified colors
    trace = []
    for i, (label, value) in enumerate(zip(labels, values)):
        trace.append(go.Bar(name=label, x=[label], y=[value], marker_color=colors[i % len(colors)]))
    
    fig = go.Figure(data=trace)
    
    # Customize layout based on user inputs
    fig.update_layout(
        title=chart_title,
        xaxis=dict(title=x_label),
        yaxis=dict(title=y_label),
        legend=dict(title=legend_title)
    )
    
    fig.show()
