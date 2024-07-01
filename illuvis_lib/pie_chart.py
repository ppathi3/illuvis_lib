import plotly.graph_objects as go

def create_custom_pie_chart(data, colors=None, chart_title='Custom Pie Chart', legend_title='Legend'):
    """
    This function creates a custom pie chart using Plotly library with customizable options.

    Parameters:
    data (dict): A dictionary where keys are categories and values are corresponding values.
    colors (list, optional): List of colors for each pie slice. If None, default colors are used.
    chart_title (str, optional): Title for the chart.
    legend_title (str, optional): Title for the legend.

    Returns:
    None. The function displays the pie chart using Plotly's show() method.

    Example:
    >>> data = {'Category1': 10, 'Category2': 20, 'Category3': 30}
    >>> colors = ['blue', 'green', 'orange']
    >>> create_custom_pie_chart(data, colors=colors, chart_title='My Custom Chart', legend_title='My Legend')
    """

    labels = list(data.keys())
    values = list(data.values())
    
    # Use default colors if not provided by user
    if colors is None:
        colors = ['blue', 'green', 'orange', 'red', 'purple']  # Default colors
    
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, marker=dict(colors=colors))])
    
    # Customize layout based on user inputs
    fig.update_layout(
        title=chart_title,
        legend_title_text=legend_title
    )
    
    fig.show()
