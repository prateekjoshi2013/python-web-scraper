import aiohttp


async def fetch_html_page(page_no,url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html_content= await response.text()
            print(f'fetched page number: {page_no} from url: {url}')
            return html_content
