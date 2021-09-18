from dataclasses import dataclass


@dataclass(init=False)
class Review:
    """
       A class to represent a Review.

       ...

       Attributes
       ----------
       title : str
           title string of the review

       author : str
           user id/name of the reviewer

       text : str
           review content

       friendliness : float
           normalized float value of the no.of star ratings for friendliness

       pricing : float
           normalized float value of the no.of star ratings for pricing

       experience : float
            normalized float value of the no.of star ratings for experience

       recommendation: str
            yes/no value of the ratings for recommendation

       customer_service: float
            normalized float value of the no.of star ratings for customer_service

       positivity_score: float
             calculated and normalized float value of the overall positivity
             review initalized with a none value
       """
    title: str
    author: str
    text: str
    friendliness: float
    pricing: float
    experience: float
    recommendation: str
    customer_service: float
    positivity_score: float
