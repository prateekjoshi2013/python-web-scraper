import logging

from textblob import TextBlob


def calculate_positivity(page_no,reviews):
    '''
    Calculates and stores the positivity_score which represents
    the positive sentiment expressed in a review in the review object
    all the ind ratings like experience,customer_service,friendliness &
    pricing are normalized to a value of 50 with recommendation being a
    yes/no normalized to a 0/50 averaged out and then divided by 50 to
    give us a rating a decimal between [0,1].Then we calculate the
    polarity using the textblob sentiment analysis library a value
    between (-1 to 1) and divide it by 2 giving us a value between
    [-0.5,0.5] and add it to the overall positivity rating

    Parameters:
            page_no (int): page no being processed
            reviews (int): list of reviews per page to be assigned positivity score

    Returns:
            reviews (str): the top min(3,len(reviews)) reviews per page
            based on positivity score calculated
    '''
    logging.info(f'started positivity calculation for page:{page_no}')
    for review in reviews:
        positivity = 0
        positivity += review.experience
        positivity += review.customer_service
        positivity += review.friendliness
        positivity += review.pricing
        positivity += 50.0 if review.recommendation else 0
        positivity /= 50 * 5
        review.positivity_score = positivity
        review.positivity_score += calculate_review_text_positivity(review.text)
    reviews.sort(key=lambda review: review.positivity_score, reverse=True)
    logging.info(f'started positivity calculation for page:{page_no}')
    return reviews[:min(3, len(reviews))]


def calculate_review_text_positivity(text_content):
    '''
     Calculates and stores the polarity score of the review text which represents
     the positive sentiment expressed in a review calculated using the
     polarity value calculated using the textblob sentiment analysis library a value
     between (-1 to 1)  and divide it by 2 giving us a value between
    [-0.5,0.5]

     Parameters:
             text_content (str): text content
     Returns:
             polarity_score (float): polarity score divided by 2
     '''
    opinion = TextBlob(text_content)
    return opinion.sentiment.polarity / 2
