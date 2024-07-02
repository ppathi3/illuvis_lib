import unittest
import pandas as pd
from illuvis_lib.scatter_plot import create_custom_scatter_plot

class TestScatterPlot(unittest.TestCase):
    def test_scatter_plot(self):
        # Example data for scatter plot
        df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [5, 6, 7, 8, 9],
            'C': ['a', 'b', 'a', 'b', 'a']
        })
        create_custom_scatter_plot(df, x_col='A', y_col='B', color_col='C', chart_title='Test Scatter Plot', x_title='X Axis', y_title='Y Axis')

if __name__ == '__main__':
    unittest.main()
