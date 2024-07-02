import unittest
from illuvis_lib.bar_chart import create_custom_bar_chart

class TestBarChart(unittest.TestCase):
    def test_bar_chart(self):
        data = {"A": 10, "B": 20, "C": 30}
        create_custom_bar_chart(data, colors=['blue'], x_label='Keys', y_label='Values', legend_title='Legend', chart_title='Sample Bar Chart')

if __name__ == '__main__':
    unittest.main()
