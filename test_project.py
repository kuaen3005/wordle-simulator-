from project import check_word, type_word


def test_check_word():
    assert check_word("HELLO" , "APPLE" , incorrect_letters = []) == "x.xvx"
    assert check_word("HAPPY" , "APPLE" , incorrect_letters = []) == "x.v.x"
    assert check_word("WRITE" , "SHORT" , incorrect_letters = []) == "x.x.x"
    assert check_word("QUITE" , "BUILD" , incorrect_letters = []) == "xvvxx"
    assert check_word("CLEAN" , "SHORT" , incorrect_letters = []) == "xxxxx"
    assert check_word("CHAIR" , "CHAIR" , incorrect_letters = []) == "vvvvv"
    assert check_word("CRIED" , "DICER" , incorrect_letters = []) == "...v."
    assert check_word("HEART" , "EARTH" , incorrect_letters = []) == "....."
def test_type_word():
    ...
def test_wordle():
    ...
