import unittest
from modulefinder import test

from day1 import Dial


class Day1Tests(unittest.TestCase):
    def test_provided_example(self):
        dial = Dial()
        test_lines = [
            "L68",
            "L30",
            "R48",
            "L5",
            "R60",
            "L55",
            "L1",
            "L99",
            "R14",
            "L82",
        ]
        for line in test_lines:
            dial.turn_dial(line)

        self.assertEqual(6, dial.zeroes)

    def test_return1_1(self):
        dial = Dial()
        test_lines = ["L50", "R50"]

        for line in test_lines:
            dial.turn_dial(line)

        self.assertEqual(1, dial.zeroes)

    def test_return1_2(self):
        dial = Dial()
        test_lines = ["L50", "L50"]

        for line in test_lines:
            dial.turn_dial(line)

        self.assertEqual(1, dial.zeroes)

    def test_return1_3(self):
        dial = Dial()
        test_lines = ["R50", "L50"]

        for line in test_lines:
            dial.turn_dial(line)

        self.assertEqual(1, dial.zeroes)

    def test_return1_4(self):
        dial = Dial()
        test_lines = ["R50", "R50"]

        for line in test_lines:
            dial.turn_dial(line)
        self.assertEqual(1, dial.zeroes)

    def test_return2_1(self):
        dial = Dial()
        test_lines = ["L150", "L50"]

        for line in test_lines:
            dial.turn_dial(line)
        self.assertEqual(2, dial.zeroes)

    def test_return2_2(self):
        dial = Dial()
        test_lines = ["L150", "R50"]

        for line in test_lines:
            dial.turn_dial(line)
        self.assertEqual(2, dial.zeroes)

    def test_return2_3(self):
        dial = Dial()
        test_lines = ["R150", "L50"]

        for line in test_lines:
            dial.turn_dial(line)
        self.assertEqual(2, dial.zeroes)

    def test_return2_4(self):
        dial = Dial()
        test_lines = ["R150", "R50"]

        for line in test_lines:
            dial.turn_dial(line)
        self.assertEqual(2, dial.zeroes)


if __name__ == "__main__":
    unittest.main()
