import unittest
from day1 import Dial

class Day1Tests(unittest.TestCase):
    
    def test_provided_example(self):
        dial = Dial()
        test_lines =["L68","L30", "R48", 
                     "L5",
                     "R60",
                     "L55",
                     "L1",
                     "L99",
                     "R14",
                     "L82"]
        for line in test_lines:
            print(f"test_line {line}")
            dial.turn_dial(line)

        self.assertEqual(3,dial.zeroes)
    
    def test_big_numbers1(self):
        dial = Dial()
        test_lines = [
                "R66",
                "L2",
                "L345",
                "R6",
                "L61",
                "R84",
                "R2"
                ]
        for line in test_lines:
            print(f"test_line: {line}")
            dial.turn_dial(line)
        self.assertEqual(1, dial.zeroes)

if __name__ == "__main__":
    unittest.main()
