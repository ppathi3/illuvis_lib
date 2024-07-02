import unittest
from illuvis_lib.radar_chart import create_custom_radar_chart

class TestRadarChart(unittest.TestCase):
    def test_radar_chart(self):
        # Example data for radar chart
        categories = ['Category1', 'Category2', 'Category3']
        values = [10, 20, 30]
        create_custom_radar_chart(data=None, categories=categories, values=values, chart_title='Test Radar Chart', color='blue')

if __name__ == '__main__':
    unittest.main()
