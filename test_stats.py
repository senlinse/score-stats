"""score-stats 的单元测试。"""

import unittest

from stats import average, highest, pass_rate, total


class TestStats(unittest.TestCase):
    def test_total(self):
        self.assertEqual(total([80, 90]), 170)

    def test_average(self):
        self.assertEqual(average([80, 90]), 85)

    def test_highest(self):
        self.assertEqual(highest([80, 90, 70]), 90)

    def test_pass_rate(self):
        self.assertEqual(pass_rate([60, 90]), 100.0)

    def test_pass_rate_boundary(self):
        # 60 分算及格
        self.assertEqual(pass_rate([60, 59]), 50.0)

    def test_pass_rate_empty(self):
        self.assertEqual(pass_rate([]), 0.0)

if __name__ == "__main__":
    unittest.main()
