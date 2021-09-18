def calculate_positivity(reviews):
    for review in reviews:
        positivity=0
        positivity+=review.experience
        positivity+=review.customer_service
        positivity+=review.friendliness
        positivity+=review.pricing
        positivity+= 50.0 if review.recommendation else 0
        positivity/=50*5
        review.positivity_score=positivity
    reviews.sort(key=lambda review:review.positivity_score,reverse=True)
    return reviews[:min(3,len(reviews))]
