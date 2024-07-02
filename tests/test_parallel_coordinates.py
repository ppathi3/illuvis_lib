import unittest
import pandas as pd
from illuvis_lib.parallel_coordinates import create_custom_parallel_coordinates

class TestParallelCoordinates(unittest.TestCase):
    def test_parallel_coordinates(self):
        # Example data for parallel coordinates plot
        df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [15, 6, 7, 18, 9],
            'C': [30, 20, 10, 40, 50],
            'D': ['X', 'Y', 'X', 'Y', 'X']
        })
        create_custom_parallel_coordinates(df, dimensions=['A', 'B', 'C'], color_col='D', chart_title='Test Parallel Coordinates')

if __name__ == '__main__':
    unittest.main()
