import pytest
from  scrape import SainsburysScraper

scraper = SainsburysScraper()

def test_loading_bad_json():
    with pytest.raises(ValueError) as err:
        scraper.get_product_list('badjson')

def test_loading_products():
    json = '[{}, {}, {}, {"productLists": [{"listStart": "<h2></h2>", "listEnd": "</ul>", "products": [{},{}] } ] } ]'
    products  = scraper.get_product_list(json)
    assert len(products) == 2

def test_missing_products():
    json = '[{}, {}, {}, {"productLists": [{"listStart": "<h2></h2>", "listEnd": "</ul>"} ] } ]'
    with pytest.raises(ValueError) as err:
        products  = scraper.get_product_list(json)

def test_calculate_sum():
    products = {"results" : [{"unit_price" : 1.5},{"unit_price" : 2}]}
    scraper.calculate_total(products)
    total = products["total"]
    assert total == 3.5

def test_missing_products():
    products = {"results" : []}
    with pytest.raises(ValueError) as err:
        products  = scraper.calculate_total(products)

