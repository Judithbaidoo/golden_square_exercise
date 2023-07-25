from lib.string_builder import *

def test_build_string_scratch() :
    word_create = StringBuilder()
    word_create.add("Hello")
    assert word_create.output() == "Hello"
    assert word_create.size() == 5

