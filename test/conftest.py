import pytest
import requests

url_page_1 = 'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/#link'


@pytest.fixture
def input_value():
    input = 39
    return input


# @pytest.fixture
# def fetched_over_network_page1():
#    res=requests.get(url_page_1)
#    text = res.text
#    print(text)
#    f=open('./test_resources/page-1.html','w')
#    f.write(text)
#    return text

@pytest.fixture
def fetched_test_page1():
    f = open('./test_resources/page-1.html', 'r')
    html_file_text = f.read()
    return html_file_text

@pytest.fixture
def fetched_test_page1():
    f = open('./test_resources/page-1.html', 'r')
    html_file_text = f.read()
    return html_file_text
