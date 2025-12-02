import unittest

from day2 import identify_invalid_id, loop_over_range, part_1


class Day2Tests(unittest.TestCase):
    def test_identify_invalid_id_True(self):
        test_id = "11"
        self.assertEqual(True, identify_invalid_id(test_id))

    def test_identify_invalid_id_Early_False(self):
        test_id = "112"
        self.assertEqual(False, identify_invalid_id(test_id))

    def test_identify_invalid_id_False(self):
        test_id = "1050"
        self.assertEqual(False, identify_invalid_id(test_id))

    def test_loop_over_range_1(self):
        range = "11-22"
        count, total = loop_over_range(range)
        self.assertEqual(2, count)

    def test_loop_over_range_2(self):
        range = "95-115"
        count, total = loop_over_range(range)
        self.assertEqual(1, count)

    def test_loop_over_range_3(self):
        range = "38593856-38593862"
        count, total = loop_over_range(range)
        self.assertEqual(1, count)

    def test_part1_provided_example(self):
        test_data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
        count, total = part_1(test_data.split(","))
        self.assertEqual(1227775554, total)


if __name__ == "__main__":
    unittest.main()
