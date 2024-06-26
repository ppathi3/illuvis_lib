import unittest
from illuvis_lib.bar_chart import create_custom_bar_chart

class TestBarChart(unittest.TestCase):
    def test_bar_chart(self):
        data = {"A": 10, "B": 20, "C": 30}
        # This is a simple test, in practice, you would use a more sophisticated testing method
        create_custom_bar_chart(data)

if __name__ == '__main__':
    unittest.main()
