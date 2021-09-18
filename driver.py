import asyncio
import concurrent.futures
import functools
import textwrap

from calculator.positivity_calculator import calculate_positivity
from parser.review_parser import reviews_parser
from scraper.html_scraper import fetch_html_page

urls = [
    'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/#link',
    'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page2/?filter=#link',
    'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page3/?filter=#link',
    'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page4/?filter=#link',
    'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page5/?filter=#link',
]


async def process_url(url, page_no, loop, executor):
    print(f'started fetching page:{page_no}')
    fetched_html_content = ''
    try:
        fetched_html_content = await fetch_html_page(page_no, url)
    except Exception as ex:
        print(f'error {ex} scraping page{page_no}')
    print(f'started parsing page:{page_no}')
    partial_reviews_parser = functools.partial(reviews_parser,page_no,fetched_html_content )
    parse_html_review_task = loop.run_in_executor(executor, partial_reviews_parser)
    result = await asyncio.gather(parse_html_review_task)
    print(f'finished parsing page:{page_no}')
    partial_calculate_positivity = functools.partial(calculate_positivity,page_no,*result)
    calculated_positivity_task = loop.run_in_executor(executor, partial_calculate_positivity)
    print(f'started positivity calculation on page:{page_no}')
    gathered_tasks = await asyncio.gather(calculated_positivity_task, loop=loop, return_exceptions=False)
    completed_gathered_tasks = []
    for sublist in gathered_tasks:
        for gathered_task in sublist:
            completed_gathered_tasks.append(gathered_task)
    return completed_gathered_tasks


async def main(urls, loop, executor):
    # create async tasks
    url_fetch_tasks = [process_url(url, i, loop, executor) for i, url in enumerate(urls, start=1)]
    gathered_tasks = await asyncio.gather(*url_fetch_tasks, loop=loop, return_exceptions=False)
    completed_gathered_tasks = []
    for sublist in gathered_tasks:
        for gathered_task in sublist:
            completed_gathered_tasks.append(gathered_task)
    return completed_gathered_tasks


def print_review(review):
    print(f"""
        AUTHOR:          {review.author}
        REVIEW--------------------------          
        {textwrap.fill(review.text,150)}
        --------------------------------
        FRIENDLINESS:    {review.friendliness}
        PRICING:         {review.pricing}
        EXPERIENCE:      {review.experience}
        RECOMMENDATION:  {review.recommendation}
        CUSTOMER_SERVICE:{review.customer_service}
        POSITIVITY_SCORE:{review.positivity_score}
    """)


if __name__ == '__main__':
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=5)
    loop = asyncio.get_event_loop()
    final_reviews = []
    try:
        most_positive_reviews = loop.run_until_complete(main(urls, loop, executor))
        for result in most_positive_reviews:
            final_reviews.append(result)
    except Exception as e:
        print(e)
    finally:
        loop.close()
    final_reviews.sort(key=lambda review: review.positivity_score, reverse=True)
    [print_review(review) for review in final_reviews[:min(3, len(final_reviews))]]
