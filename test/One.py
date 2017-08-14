import unittest
from source.One import get_number_plate


class NumberPlateTests(unittest.TestCase):

    def test_true_positive(self):
        # should get the explicit number plate in the sentence
        sentence = 'I saw a KCA 199A on the highway'
        self.assertEqual(get_number_plate(sentence), 'KCA 199A')

    def test_case_insensitive(self):
        # should extract the number plate even whether in upper/lower/mixed case
        sentence = "Mercy just bought kBA 951j"
        self.assertEqual(get_number_plate(sentence), 'KBA 951J')

    def test_invalid_number_plate(self):
        # should fail if a letter isn't the last character
        sentence = "KBA 9511 was bought by Mercy"
        self.assertEqual(get_number_plate(sentence), 'NO PLATE')

    def test_no_number_plate_in_sentence(self):
        # should return 'NO PLATE' if there isn't any mention of a number plate in sentence
        sentence = 'She sells sea shells at the seas shore'
        self.assertEqual(get_number_plate(sentence), 'NO PLATE')

if __name__ == '__main__':
    unittest.main()
