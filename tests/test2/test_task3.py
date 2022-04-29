import pytest
from src.test2.task3 import count_top_words, count_sentences


def test_sentence():
    assert count_sentences("tests/test2/Data/test.txt") == 12


def test_simple_word_counter():
    assert count_top_words("tests/test2/Data/test.txt", 1) == ["to"]


def test_pro_word_counter():
    assert count_top_words("tests/test2/Data/test.txt", 10) == [
        "to",
        "are",
        "women",
        "in",
        "so",
        "of",
        "their",
        "children",
        "that",
        "a",
    ]
