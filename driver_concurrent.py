import asyncio
import concurrent.futures
import functools
import textwrap
import logging
import time
from calculator.positivity_calculator import calculate_positivity
from parser.review_parser import reviews_parser
from scraper.html_scraper import fetch_html_page

logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

urls = [
    'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/#link',
    'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page2/?filter=#link',
    'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page3/?filter=#link',
    'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page4/?filter=#link',
    'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page5/?filter=#link',
]


async def process_url(url, page_no, loop, executor):
    """
    Method to create an async/await task flow which gets executed on the loop and executor
    which is responsible for calling different methods on the asynchronus data flow as well
    as long running cpu bound tasks.
    It follows the following flow:
        fetch_html_page -> parse_html_review_task -> calculate_positivity
        (ASYNCHRONUS)        (MULTITHREADED)            (MULTITHREADED)
        (I/O BOUND)            (CPU BOUND)                 (CPU BOUND)

    Parameters
    ----------
        url : List[str]
            url to be fetched from the network
        page_no: int
            page number being processed
        loop: AbstractAsyncLoop
                event loop for running async coroutines

        executor: ProcessPoolExecutor
                    uses the executor pool created for multiple
                    processes running cpu intesinve code in parallel

        Returns: completed_gathered_tasks: Future[List[Review]]
                    returns the future with top three positive reviews from each object

    """
    fetched_html_content = ''
    try:
        fetched_html_content = await fetch_html_page(page_no, url)
    except Exception as ex:
        logging.error(f'error {ex} scraping page{page_no}')
    partial_reviews_parser = functools.partial(reviews_parser, page_no, fetched_html_content)
    parse_html_review_task = loop.run_in_executor(executor, partial_reviews_parser)
    result = await asyncio.gather(parse_html_review_task)
    partial_calculate_positivity = functools.partial(calculate_positivity, page_no, *result)
    calculated_positivity_task = loop.run_in_executor(executor, partial_calculate_positivity)
    gathered_tasks = await asyncio.gather(calculated_positivity_task, loop=loop, return_exceptions=False)
    completed_gathered_tasks = []
    for sublist in gathered_tasks:
        for gathered_task in sublist:
            completed_gathered_tasks.append(gathered_task)
    return completed_gathered_tasks


async def main(urls, loop, executor):
    """
    Method to create the async tasks for the event loop for chained coroutine
    which is responsible for calling different methods on the asynchronus data flow

    Parameters
    ----------
        urls : List[str]
            list of urls to be fetched from the network

        loop: AbstractAsyncLoop
                event loop for running async coroutines

        executor: ProcessPoolExecutor
                    uses the executor pool created for multiple
                    processes running cpu intesinve code in parallel

        Returns: completed_gathered_tasks: Future[List[Review]]
                    returns the future with top three positive reviews from each object

    """
    # create async tasks
    url_fetch_tasks = [process_url(url, i, loop, executor) for i, url in enumerate(urls, start=1)]
    gathered_tasks = await asyncio.gather(*url_fetch_tasks, loop=loop, return_exceptions=False)
    completed_gathered_tasks = []
    for sublist in gathered_tasks:
        for gathered_task in sublist:
            completed_gathered_tasks.append(gathered_task)
    return completed_gathered_tasks


def print_review(review):
    """
    Method to print the three most positive reviews with formatting

    Parameters
    ----------
        review : Review
            Review object to be printed

    """
    print(f"""
        AUTHOR:          {review.author}
        REVIEW--------------------------          
        {textwrap.fill(review.text, 150)}
        --------------------------------
        FRIENDLINESS:    {review.friendliness}
        PRICING:         {review.pricing}
        EXPERIENCE:      {review.experience}
        RECOMMENDATION:  {review.recommendation}
        CUSTOMER_SERVICE:{review.customer_service}
        POSITIVITY_SCORE:{review.positivity_score}
    """)


if __name__ == '__main__':
    """
    The main driver program which creates executor pool for multprocessing 
    for execution of sequential cpu bound tasks like parsing the web page , 
    calculating the positivity of reviews in parallel and initializes 
    the event loop for running asynchronous I/O bound tasks like fetching 
    html from the urls.
    prints the three most positive reviews from the pages provided
    
        ****************************** IMPORTANT***************************************
            dunder main block is needed so that the process executor pool does not get 
            created recursively when the child processes import the script from the 
            parent process as the dunder main block gets executed only when this file 
            is run and not imported
        *******************************************************************************
    """
    start_time = time.perf_counter()
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
    logging.info(f'TIME_TAKEN:{time.perf_counter() - start_time}')
