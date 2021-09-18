import logging

import aiohttp


async def fetch_html_page(page_no, url):
    '''
        Returns the downloaded content html content of the url.
        It is a coroutine using asynchronus aiohttp library which can
        fetch pages asynchronously through the event loop.

                Parameters:
                        page_no (int): page no beign downloaded
                        url (str): url of the page getting downloaded

                Returns:
                        html_content (str): html content of the url provided
        '''
    logging.info(f'start fetching page number: {page_no} from url: {url}')
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html_content = await response.text()
            logging.info(f'fetched page number: {page_no} from url: {url}')
            return html_content
