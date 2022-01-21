from app import hello, bubble_sort
from app import extract_sentiment
from app import text_contain_word
import pytest


def test_hello():
    got = hello("Aleksandra")
    want = "Hello Aleksandra"

    assert got == want


testdata1 = ["I think today will be a great day"]


@pytest.mark.parametrize('sample', testdata1)
def test_extract_sentiment(sample):

    sentiment = extract_sentiment(sample)

    assert sentiment > 0


testdata2 = [
    ('There is a duck in this text', 'duck', True),
    ('There is nothing here', 'duck', False)
    ]


@pytest.mark.parametrize('sample, word, expected_output', testdata2)
def test_text_contain_word(sample, word, expected_output):

    assert text_contain_word(word, sample) == expected_output


class TestBubbleSort:

    valid_data = [
        ([1] * 6, [1] * 6),  # equal elements
        ([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]),  # sorted list
        ([6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6]),  # reversed list
        ([6, 2, 5, 3, 4, 1], [1, 2, 3, 4, 5, 6]),  # mixed list
        ([-6, 1, -4, 2, 3, 5], [-6, -4, 1, 2, 3, 5]),  # list witch negative numbers
        ([], [])  # empty list
    ]


    invalid_data = [
        None,  # None as argument
        "text",  # text as argument
        [1, "Text", 6],  # mixed int and string
        [6, None, 1]  # None in list
    ]


    @pytest.mark.parametrize('to_sort, correct', valid_data)
    def test_with_valid_data(self, to_sort, correct):
        to_sort = bubble_sort(to_sort)
        assert to_sort == correct

    @pytest.mark.parametrize('to_sort', invalid_data)
    def test_with_invalid_data(self, to_sort):
        to_sort = bubble_sort(to_sort)
        assert to_sort is None



