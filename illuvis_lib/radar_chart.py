import plotly.graph_objects as go

def create_custom_radar_chart(data, categories, values, chart_title='Custom Radar Chart', color='blue'):
    """
    This function creates a custom radar chart using the Plotly library with customizable options.

    Parameters:
    data (dict): A dictionary where keys are categories and values are corresponding values.
    categories (list): A list of category names.
    values (list): A list of values corresponding to the categories.
    chart_title (str, optional): Title for the chart.
    color (str, optional): Color for the radar chart.

    Returns:
    None. The function displays the radar chart using Plotly's show() method.
    """

    fig = go.Figure(data=go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        marker=dict(color=color)
    ))
    
    fig.update_layout(
        title=chart_title,
        polar=dict(
            radialaxis=dict(
                visible=True
            )
        )
    )
    
    fig.show()
