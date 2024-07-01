import unittest
from illuvis_lib.pie_chart import create_custom_pie_chart

class TestBarChart(unittest.TestCase):
    def test_pie_chart(self):
        data = {"A": 10, "B": 20, "C": 30}
        # This is a simple test, in practice, you would use a more sophisticated testing method
        create_custom_pie_chart(data, chart_title='My Custom Pie Chart', legend_title='My Legend')

if __name__ == '__main__':
    unittest.main()
