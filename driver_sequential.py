import time

import requests

from calculator.positivity_calculator import calculate_positivity
from parser.review_parser import reviews_parser

urls = [
    'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/#link',
    'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page2/?filter=#link',
    'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page3/?filter=#link',
    'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page4/?filter=#link',
    'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page5/?filter=#link',
]
if __name__ == '__main__':
    start_time = time.perf_counter()
    collected_positive_reviews = []
    for i, url in enumerate(urls, start=1):
        res = requests.get(url)
        text = res.text
        reviews = reviews_parser(i, text)
        positivitied_reviews = calculate_positivity(i, reviews)
        for positive_review in positivitied_reviews:
            collected_positive_reviews.append(positive_review)
    collected_positive_reviews.sort(key=lambda review: review.positivity_score, reverse=True)
    [print(pos_review) for pos_review in collected_positive_reviews[:min(3, len(collected_positive_reviews))]]
    print(f'TIME ELAPSED:{time.perf_counter() - start_time}')
