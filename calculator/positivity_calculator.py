import logging

from textblob import TextBlob


def calculate_positivity(page_no,reviews):
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
    opinion = TextBlob(text_content)
    return opinion.sentiment.polarity / 2
