import unittest

from source.PlateCounter import count_plates


class PlateCounterTests(unittest.TestCase):

    def test_invalid_inputs(self):
        # make sure that both plates supplies are valid Kenyan plates
        self.assertEqual(count_plates("KBA 123J", "KAY F237"), "INVALID PLATE")

    def test_count(self):
        self.assertEqual(count_plates("KBA 049A", "KBA 50A"), 1)
        self.assertEqual(count_plates("KBE 050A", "KBE 098A"), 48)
        self.assertEqual(count_plates("KBD 050A", "KBD 250A"), 200)
        self.assertEqual(count_plates("KBC 099A", "KBD 099A"), 1000)

if __name__ == '__main__':
    unittest.main()
