"""score-stats 的单元测试。"""

import unittest

from stats import average, highest, total


class TestStats(unittest.TestCase):
    def test_total(self):
        self.assertEqual(total([80, 90]), 170)

    def test_average(self):
        self.assertEqual(average([80, 90]), 85)

    def test_highest(self):
        self.assertEqual(highest([80, 90, 70]), 90)


if __name__ == "__main__":
    unittest.main()
