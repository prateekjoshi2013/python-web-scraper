import pytest

from calculator.positivity_calculator import calculate_positivity
from models.review import Review
from test.conftest import create_review_collection


@pytest.mark.parametrize("page_no,positivity_score",[(1,0),(3,0)])
def test_positivity_score_calculation_logic(page_no,create_review_collection,positivity_score):
    reviews=calculate_positivity(page_no,create_review_collection)
    assert [review.positivity_score for review in  reviews]==[1.409375, 1.38125, 1.34765625]