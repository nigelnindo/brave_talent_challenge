import unittest

from source.PlateCounter import count_plates


class PlateCounterTests(unittest.TestCase):

    def test_invalid_inputs(self):
        # make sure that both plates supplies are valid Kenyan plates
        self.assertEqual(count_plates("KBA 123J", "KAY F237"), "INVALID PLATE")

    def test_count(self):
        # values that come after one another should have a difference of 1
        self.assertEqual(count_plates("KBA 049A", "KBA 050A"), 1)
        # values different in the tens should still calculate correctly
        self.assertEqual(count_plates("KBE 050A", "KBE 098A"), 48)
        # value different in the hundreds should still calculate correctly
        self.assertEqual(count_plates("KBD 050A", "KBD 250A"), 200)
        # changing last letter of plate by moving to the next largest figure should have a difference of one
        self.assertEqual(count_plates("KAA 999A", "KAA 001B"), 1)
        # moving to new last letter of 'prefix' should result in a difference of one
        self.assertEqual(count_plates("KAA 999Z", "KAB 001A"), 1)
        # moving to first letter of 'prefix' should result in a difference of one
        self.assertEqual(count_plates("KAZ 999Z", "KBA 001A"), 1)


if __name__ == '__main__':
    unittest.main()
