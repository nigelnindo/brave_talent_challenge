def split_sentence(sentence):
    return sentence.split()


def clean_words(word_list):
    return word_list


def is_plate_prefix(word):
    print 'check for prefix: ' + word
    # rule out words that don't begin with 'K'
    if word[0] != "K":
        print word + " does not begin with 'K'"
        return False
    # rule out words which don't equal 3 chars
    if len(word) != 3:
        print word + "does not equal 3 chars"
        return False
    # rule out words with numbers
    if not word.isalpha():
        return False
    return True


def is_plate_suffix(word):
    print 'check for suffix'
    # rule out words which don't equal 4 chars
    if len(word) != 4:
        print word + " does not equal 4 chars"
        return False
    # rule out words that don't end with a letter
    if not word[-1:].isalpha():
        print word + " does not end with a letter"
        return False
    # make sure that the first 3 chars are numbers
    if not word[:3].isdigit():
        return False
    return True


def search_for_plate(word_list):
    plate_prefix = {'word': "", 'index': 0}  # keep index, because prefix has to come right before suffix
    plate_suffix = ""
    for index, word in enumerate(word_list):
        if plate_prefix['word'] == "":
            if is_plate_prefix(word):
                plate_prefix['word'] = word
                plate_prefix['index'] = index
            else:
                pass  # no need to search for plate suffix if we haven't yet found a valid plate prefix
        else:
            if plate_suffix == "":
                # suffix should only be searched for if current index minus prefix index is one
                if index - plate_prefix['index'] == 1:
                    if is_plate_suffix(word):
                        plate_suffix = word
                else:
                    # begin search for a new prefix
                    if is_plate_prefix(word):
                        plate_prefix['word'] = word
                        plate_prefix['index'] = index
            else:
                pass  # do nothing if we already have a prefix/suffix pair
    if plate_suffix != "":
        return plate_prefix['word'] + " " + plate_suffix
    else:
        return 'NO PLATE'


def get_number_plate(sentence):
    words = split_sentence(sentence.upper())
    return search_for_plate(clean_words(words))

print get_number_plate('KBA 951j was bought by Mercy')
