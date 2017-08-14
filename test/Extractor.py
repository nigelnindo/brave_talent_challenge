import unittest
from source.Extractor import get_number_plate

NEGATIVE_RESULT = 'NO PLATE'


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
        self.assertEqual(get_number_plate(sentence), NEGATIVE_RESULT)
        # should fail if any of first three characters in plate suffix is a string
        sentence_2 = "KBA 9A5J was bought by Mercy"
        self.assertEqual(get_number_plate(sentence_2), NEGATIVE_RESULT)
        # should fail if any of the characters in plate suffix is a number
        sentence_3 = "KB3 951J was bought by Mercy"
        self.assertEqual(get_number_plate(sentence_3), NEGATIVE_RESULT)

    def test_no_number_plate_in_sentence(self):
        # should return 'NO PLATE' if there isn't any mention of a number plate in sentence
        sentence = 'She sells sea shells at the sea shore'
        self.assertEqual(get_number_plate(sentence), NEGATIVE_RESULT)

    def test_two_positive_plate_prefixes(self):
        # should ignore 'Ken', which is a positive prefix, but is a name
        sentence = "Yesterday, Ken was driving a KBC 367A"
        self.assertEqual(get_number_plate(sentence), 'KBC 367A')

if __name__ == '__main__':
    unittest.main()
