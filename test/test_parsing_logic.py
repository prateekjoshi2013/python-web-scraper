from collections import namedtuple

import pytest

from models.review import Review
from parser.review_parser import reviews_parser


@pytest.mark.parametrize("page_no,html_content",[(1,None,), (2,'',), (3,'iuhei iufehihf iehf',)])
def test_parsing_logic_page_with_empty_content(page_no,html_content):
    reviews = reviews_parser(0,None)
    assert len(reviews)==0



@pytest.mark.parametrize("page_no",[1,2,3,4,5])
def test_parsing_logic_page(page_no):
    f = open(f'./test_assets/page-{page_no}.html', 'r')
    html_file_text = f.read()
    f.close()
    reviews = reviews_parser(3,html_file_text)
    assert len(reviews) == 10


