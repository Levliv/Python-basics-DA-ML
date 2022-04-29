import re
from collections import Counter
from typing import List

letter_pattern = "[а-яА-Яa-zA-Z]"
word_pattern = re.compile("[A-Яа-яA-Za-z]+")
sentence_pattern = re.compile("[.!?]+")


def count_top_words(string: str, top: int = 10) -> List[int]:
    """
    Counts 10-top words in the given text.
    """
    words = {}
    with open(string) as file:
        for line in file:
            for word in word_pattern.findall(line):
                word_lower = word.lower()
                if word_lower not in words:
                    words[word_lower] = 0
                words[word_lower] += 1
    return [word for word, frequency in Counter(words).most_common(top)]


def count_sentences(string: str) -> int:
    """
    Counts sentences in the given text.
    """
    counter = 0
    with open(string) as file:
        for line in file:
            counter += len(sentence_pattern.findall(line))
    return counter
