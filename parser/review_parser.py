import logging

from bs4 import BeautifulSoup

from models.review import Review


def reviews_parser(page_no, html_page_string):
    '''
        Returns the parsed reviews from html content provided as a string
        of the provided page no.Since it is a cpu intensive operation reading
        the html page in memory and extracting info from it using BeautifulSoup
        library,it is executed by the multiprocessing executor for parallelism.

                Parameters:
                        page_no (int): page no beign downloaded
                        html_page_string (str): html content of the page being downloaded

                Returns:
                        reviews_list (list[Review]): a list of extracted reviews object
    '''
    logging.info(f'started parsing page:{page_no}')
    review_list = []
    if html_page_string:
        soup = BeautifulSoup(html_page_string, 'html.parser')
        review_entries = soup.find_all('div', class_="review-entry")
        for review_entry in review_entries:
            review = review_parser(review_entry)
            review_list.append(review)
    logging.info(f'finished parsing page:{page_no}')
    return review_list


def review_parser(review_entry):
    '''
        extracts a single review element and transforms it into a review object
        from a review entry element extracted.
                Parameters:
                        review_entry (html_element): html element from beautiful soup
                Returns:
                        review (Review): a Review with values transformed from html_element
    '''
    if review_entry:
        review_content = review_entry.find('p', class_='review-content')
        review_author = review_entry.find('span')
        review_title = review_entry.find('h3')
        review_ratings_all_element = review_entry.find('div', class_='review-ratings-all')
        review_elements = review_ratings_all_element.find_all('div', class_='tr')
        ratings_map = ratings_parser(review_elements)
        review = Review()
        review.title = review_title.text if review_title else ''
        review.author = review_author.text if review_author else ''
        review.text = review_content.text if review_content else ''
        review.customer_service = float(ratings_map.get('Customer Service', 0.0))
        review.friendliness = float(ratings_map.get('Friendliness', 0.0))
        review.pricing = float(ratings_map.get('Pricing', 0.0))
        review.experience = float(ratings_map.get('Overall Experience', 0.0))
        review.recommendation = ratings_map.get('Recommend Dealer', None)
        review.positivity_score = None
    return review


def ratings_parser(review_elements):
    '''
        extracts and normalizes review ratings and transforms it into a ratings dictionary
        from individual review entry elements extracted.
                Parameters:
                        review_elements (html_element): html elements containing individual ratings section
                Returns:
                        ratings_map (dict): a ratings map with values extracted and transformed html_element
    '''
    ratings_map = {}
    if review_elements:
        for ind_review_element in review_elements:
            if ind_review_element:
                rating_elements = ind_review_element.find_all('div')
                rating_desc_elem = rating_elements[0]
                rating_elem = rating_elements[1]
                if rating_desc_elem.text == "Recommend Dealer":
                    ratings_map[rating_desc_elem.text] = rating_elem.text.strip()
                else:
                    for class_string in rating_elem['class']:
                        if not class_string.startswith('rating-static-indv') and class_string.startswith('rating-'):
                            ratings_map[rating_desc_elem.text] = class_string.split("-")[1]
    return ratings_map
