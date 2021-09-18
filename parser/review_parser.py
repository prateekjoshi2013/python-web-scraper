from bs4 import BeautifulSoup

from models.review import Review


def reviews_parser(page_no,html_page_string):
    review_list = []
    if html_page_string:
        soup = BeautifulSoup(html_page_string, 'html.parser')
        review_entries = soup.find_all('div', class_="review-entry")
        for review_entry in review_entries:
            review = review_parser(review_entry)
            review_list.append(review)
    return review_list


def review_parser(review_entry):
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
