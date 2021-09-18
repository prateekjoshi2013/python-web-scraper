from dataclasses import dataclass


@dataclass(init=False)
class Review:
    title:str
    author:str
    text:str
    friendliness:float
    pricing:float
    experience:float
    recommendation:str
    customer_service:float
    positivity_score:float
