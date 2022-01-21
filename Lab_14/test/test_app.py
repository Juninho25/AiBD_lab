from app import hello
from app import extract_sentiment
from app import text_contain_word
from app import bubble_sort
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


testdata3 = [
    [[1, 5, 7, 9, 2, 4, 6, 8, 3], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
    [[9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
    [[7, 8, 9, 4, 5, 6, 1, 2, 3], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
    [[1, 9, 2, 8, 3, 7, 4, 6, 5], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
    [[3, 5, 7, 1, 9, 2, 6, 4, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9]]
]


@pytest.mark.parametrize('sample, expected_output', testdata3)
def test_bubble_sort(sample, expected_output):

    assert bubble_sort(sample) == expected_output