from collections import namedtuple

import pytest
import requests

from models.review import Review

url_page_1 = 'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/#link'
url_page_2 = 'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page2/?filter=#link'
url_page_3 = 'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page3/?filter=#link'
url_page_4 = 'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page4/?filter=#link'
url_page_5 = 'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page5/?filter=#link'


# @pytest.fixture
# def fetched_over_network_page1():
#     res = requests.get(url_page_1)
#     text = res.text
#     print(text)
#     f = open('./test_resources/page-2.html', 'w')
#     f.write(text)
#     return text


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
    f = open('test_assets/page-1.html', 'r')
    html_file_text = f.read()
    return html_file_text


@pytest.fixture
def create_reviews():
    f = open('test_assets/page-1.html', 'r')
    html_file_text = f.read()
    return html_file_text

@pytest.fixture
def create_review_collection():
    Review_Tuple = namedtuple('Review_Tuple',
                              'title,author,text,friendliness,pricing,experience,recommendation,customer_service,positivity_score')
    reviews1 = [Review_Tuple(title='"Loved our experience! Great listener! Understood what we..."', author='- Brandy',
                             text='Loved our experience! Great listener! Understood what we needed as a geowing family and got us into the perfect fit. Always listened to my life story. ',
                             friendliness=50.0, pricing=50.0, experience=50.0, recommendation='Yes',
                             customer_service=50.0,
                             positivity_score=1.409375),
                Review_Tuple(title='"Awesome service, Adrian was great to work with I told him..."',
                             author='- laura92689',
                             text='Awesome service, Adrian was great to work with I told him what I wanted and he showed me the best car Thank you so much!',
                             friendliness=50.0, pricing=50.0, experience=50.0, recommendation='Yes',
                             customer_service=50.0,
                             positivity_score=1.38125),
                Review_Tuple(title='"Adrian is the best… he helped get everything in order to..."',
                             author='- scero1996',
                             text='Adrian is the best… he helped get everything in order to buy our Jeep and had everything ready when we walked in to the dealership!!! Great experience!!!',
                             friendliness=50.0, pricing=50.0, experience=50.0, recommendation='Yes',
                             customer_service=50.0,
                             positivity_score=1.34765625)]

    reviews2 = [Review_Tuple(title='"Loved our experience! Great listener! Understood what we..."', author='- Brandy',
                             text='Loved our experience! Great listener! Understood what we needed as a geowing family and got us into the perfect fit. Always listened to my life story. ',
                             friendliness=50.0, pricing=50.0, experience=50.0, recommendation='Yes',
                             customer_service=0.0,
                             positivity_score=1.409375),
                Review_Tuple(title='"Awesome service, Adrian was great to work with I told him..."',
                             author='- laura92689',
                             text='Awesome service, Happy good best  was great to work with I told him what I wanted and he showed me the best car Thank you so much!',
                             friendliness=50.0, pricing=50.0, experience=50.0, recommendation='Yes',
                             customer_service=50.0,
                             positivity_score=1.38125),
                Review_Tuple(title='"the best… he helped get everything in order to..."', author='- scero1996',
                             text='Adrian is the worst bad not good too slow is  ',
                             friendliness=50.0, pricing=50.0, experience=50.0, recommendation='Yes',
                             customer_service=50.0,
                             positivity_score=1.34765625)]
    reviews = []
    for review_tuple in reviews1:
        review = Review()
        review.title = review_tuple.title
        review.author = review_tuple.author
        review.text = review_tuple.text
        review.friendliness = review_tuple.friendliness
        review.pricing = review_tuple.pricing
        review.experience = review_tuple.experience
        review.customer_service = review_tuple.customer_service
        review.positivity_score = review_tuple.positivity_score
        review.recommendation=review_tuple.recommendation
        reviews.append(review)
    return reviews

