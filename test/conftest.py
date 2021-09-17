import pytest
import requests

url_page_1 = 'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/#link'
url_page_2 = 'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page2/?filter=#link'
url_page_3 = 'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page3/?filter=#link'
url_page_4 = 'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page4/?filter=#link'
url_page_5 = 'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page5/?filter=#link'


@pytest.fixture
def input_value():
    input = 39
    return input


@pytest.fixture
def fetched_over_network_page1():
    res = requests.get(url_page_1)
    text = res.text
    print(text)
    f = open('./test_resources/page-2.html', 'w')
    f.write(text)
    return text


# @pytest.fixture
# def fetched_over_network_page2_4():
#     urls=[url_page_1,url_page_2,url_page_3,url_page_4,url_page_5]
#     for i,url in enumerate(urls,start=1):
#         print(i,url)
#         res=requests.get(url)
#         text = res.text
#         f=open(f'./test_resources/page-{i}.html','w')
#         f.write(text)
#         f.close()
#     return None

@pytest.fixture
def fetched_test_page1():
    f = open('test_resources/page-1.html', 'r')
    html_file_text = f.read()
    return html_file_text


@pytest.fixture
def fetched_test_page1():
    f = open('test_resources/page-1.html', 'r')
    html_file_text = f.read()
    return html_file_text


@pytest.fixture
def fetched_test_page2():
    f = open('test_resources/page-2.html', 'r')
    html_file_text = f.read()
    return html_file_text


@pytest.fixture
def fetched_test_page3():
    f = open('test_resources/page-3.html', 'r')
    html_file_text = f.read()
    return html_file_text


@pytest.fixture
def fetched_test_page4():
    f = open('test_resources/page-4.html', 'r')
    html_file_text = f.read()
    return html_file_text


@pytest.fixture
def fetched_test_page5():
    f = open('test_resources/page-5.html', 'r')
    html_file_text = f.read()
    return html_file_text
