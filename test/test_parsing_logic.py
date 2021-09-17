import pytest

from parser.review_parser import reviews_parser


@pytest.mark.parametrize("html_content",[(None,), ('',), ('iuhei iufehihf iehf',)])
def test_parsing_logic_page_with_empty_content(html_content):
    reviews = reviews_parser(None)
    assert len(reviews)==0



def test_parsing_logic_page_1(fetched_test_page1):
    reviews = reviews_parser(fetched_test_page1)
    assert len(reviews) == 10


def test_parsing_logic_page_2(fetched_test_page2):
    reviews = reviews_parser(fetched_test_page2)
    assert len(reviews) == 10


def test_parsing_logic_page_3(fetched_test_page3):
    reviews = reviews_parser(fetched_test_page3)
    assert len(reviews) == 10


def test_parsing_logic_page_4(fetched_test_page4):
    reviews = reviews_parser(fetched_test_page4)
    assert len(reviews) == 10


def test_parsing_logic_page_5(fetched_test_page5):
    reviews = reviews_parser(fetched_test_page5)
    assert len(reviews) == 10
