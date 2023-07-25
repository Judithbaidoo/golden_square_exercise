from lib.counter import *

def test_counting_numbers():
    initial_num = Counter()
    add_number = initial_num.add(3)
    assert initial_num.report() == "Counted to 3 so far."
