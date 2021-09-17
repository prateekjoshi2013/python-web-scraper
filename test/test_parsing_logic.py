from bs4 import BeautifulSoup
def test_parsing_logic(fetched_test_page1):
   soup=BeautifulSoup(fetched_test_page1,'html.parser')
   review_entries=soup.find_all('div',class_="review-entry")
   review_content=review_entries[0].find('p',class_='review-content')
   review_ratings_all_element=review_entries[0].find('div',class_='review-ratings-all')
   review_elements=review_ratings_all_element.find_all('div',class_='tr')
   ratings_map={}
   for ind_review_element in review_elements:
      rating_elements=ind_review_element.find_all('div')
      rating_desc_elem=rating_elements[0]
      rating_elem=rating_elements[1]
      if rating_desc_elem.text=="Recommend Dealer":
         ratings_map[rating_desc_elem.text]=rating_elem.text.strip()
      else:
         for class_string in rating_elem['class']:
            if not class_string.startswith('rating-static-indv') and class_string.startswith('rating-'):
               ratings_map[rating_desc_elem.text] = class_string.split("-")[1]

   print(review_content)



