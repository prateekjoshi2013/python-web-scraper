import asyncio
import concurrent.futures

from calculator.positivity_calculator import calculate_positivity
from parser.review_parser import reviews_parser
from scraper.html_scraper import fetch_html_page

urls=[
  'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/#link',
  'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page2/?filter=#link',
  'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page3/?filter=#link',
  'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page4/?filter=#link',
  'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page5/?filter=#link',
]

async def process_url(url,page_no,loop,executor):
    print(f'started fetching page:{page_no}')
    fetched_html_content=await fetch_html_page(page_no,url)
    print(f'started parsing page:{page_no}')
    parse_html_review_task=loop.run_in_executor(executor, reviews_parser,fetched_html_content )
    result = await asyncio.gather(parse_html_review_task)
    print(f'finished parsing page:{page_no}')
    calculated_positivity_task=loop.run_in_executor(executor,calculate_positivity,*result)
    print(f'started positivity calculation on page:{page_no}')
    calculated_positivity_reviews,pending = await asyncio.wait([calculated_positivity_task])
    print(f'finished positivity calculation on page:{page_no}')
    return calculated_positivity_reviews


async def main(urls,loop,executor):
    # create async tasks
    url_fetch_tasks=[process_url(url,i,loop,executor) for i,url in enumerate(urls,start=1)]
    completed,pending = await asyncio.wait(url_fetch_tasks,return_when=asyncio.ALL_COMPLETED)
    # print(completed,pending)
    return completed



if __name__=='__main__':
    executor=concurrent.futures.ProcessPoolExecutor(max_workers=5)
    loop=asyncio.get_event_loop()
    final_result=[]
    try:
        most_positive_reviews = loop.run_until_complete(main(urls,loop,executor))
        for msp_review in most_positive_reviews:
            msp1= msp_review.result()
            for msp in msp1:
                for msp_r in msp.result():
                    final_result.append(msp_r)

    finally:
        loop.close()
    print(final_result)
