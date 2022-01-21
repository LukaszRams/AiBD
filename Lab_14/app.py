from textblob import TextBlob
from typing import List


def hello(name):
    output = f'Hello {name}'
    return output


def extract_sentiment(text):
    text = TextBlob(text)

    return text.sentiment.polarity


def text_contain_word(word: str, text: str):
    return word in text


def bubble_sort(to_sort: List[int]) -> List[int]:
    if not isinstance(to_sort, list):
        return None

    for elem in to_sort:
        if not isinstance(elem, (int, float)):
            return None

    n: int = len(to_sort)

    for i in range(n):
        for j in range(n-1-i):
            if to_sort[j] > to_sort[j+1]:
                to_sort[j], to_sort[j+1] = to_sort[j+1], to_sort[j]

    return to_sort




