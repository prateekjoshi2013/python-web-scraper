from calculator.positivity_calculator import calculate_review_text_positivity


def test_sentiment_analysis():
    polarity=calculate_review_text_positivity("Wow, NLTK is really powerful!")
    assert polarity != 0
