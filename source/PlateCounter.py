from Extractor import get_number_plate


def get_alphabet_index(character):
    alphabet = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
                'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,
                'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    return alphabet[character]


def get_numeric_index(number):
    return number + 1


def compute(tagged_list):
    second_suffix_val = tagged_list[1]
    if tagged_list[0] > 1:
        print 'Set second suffix val to 26'
        second_suffix_val = 26
    suffix_val = (tagged_list[2] + (999 * (tagged_list[3] - 1)))
    return (tagged_list[0] * second_suffix_val * 999 * 26) - (999 * 26 - suffix_val)


def clean_and_tag(number_plate):
    no_whitespace = "".join(number_plate.split())
    char_list = list(no_whitespace[1:])  # create a list of characters while excluding the first character 'K'
    # tag both numbers (0-9[1-10]) and alphabets (A-Z[1-26])
    tagged_list = [get_alphabet_index(char_list[0]),    # K[X]X DDDX
                   get_alphabet_index(char_list[1]),    # KX[X] DDDX
                   int(''.join(char_list[2:5])),        # KXX [DDD]X
                   get_alphabet_index(char_list[5])]    # KXX DDD[X]
    return tagged_list


def count_plates(start_plate, end_plate):
    if get_number_plate(start_plate) == 'NO PLATE' or get_number_plate(end_plate) == 'NO PLATE':
        return 'INVALID PLATE'
    start_value = compute(clean_and_tag(start_plate))
    end_value = compute(clean_and_tag(end_plate))
    print start_value
    print end_value
    if start_value > end_value:
        return start_value - end_value
    else:
        return end_value - start_value

print count_plates("KAZ 999Z", "KBA 001A")

"""
Assumptions:
-> Number plate with three zeros KXX 000X is not allowed

KAA 001A => (1)(1) (999)(1) + (1) = 1000
KAA 999A => (1)(1) (999)(1) + (999) = 1998
KAA 001B => (1)(1) (999)(2) + (1)  = 1999
KAA 999B => (1)(1) (999)(2) + 999 = 2995
KAC 999B => (1)(3) ((999)(2) + 999) = 8991

KBA 049A => (2)(1) (999)(49) + 49 = 49000
KBA 050A => (2)(1) (999)(50) + 50 = 49950

KBB 050Z => (KBA 999Z) + 050Z
         => (2 * 1 * 999 * 26) + 050Z
         => (51948) + (50 + (999 * 26))
KBC 001A => (KBB 999Z) + 001A
         => (2 * 2 * 999 * 26) + 001A
         => (103896) + (1 + (999 * 1))

KBA 049A => (KAA 999Z) + 049A
         => (1 * 1 * 999 * 26) + (49 + (999 * [a-1]))
         => (25974) + (49 + 0)
         RHS = ([3-num] + (999 * [value of last alphabet minus one]))
KBA 050A => (KAA 999Z) + 050A
         => (1 * 1 * 999 * 26) + (50 + (999 * 1))

RHS := KBA049A => KBA999Z - suffix
    := KAB049A => KAB999Z - suffix
"""

"""
Final algorithm:
(prefix_1 * prefix_2 * max_val) - (max_val - RHS)
KAA001A => KAA999Z
        => (1 * 1 * 25974) - (25974 - RHS)
        => (25974) - (25974 - 1)
        => 1
"""