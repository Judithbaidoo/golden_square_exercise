from lib.gratitudes import * 

def test_gratitudes_word():
    gratitude_arr = Gratitudes()
    gratitude_arr.add("Life")
    assert gratitude_arr.format() == "Be grateful for: Life"
    