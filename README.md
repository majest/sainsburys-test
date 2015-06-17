To set up the environment it's best to use virtualenv

```
$>virtualenv venv
$>. ./venv/bin/activate
```

Install application dependencies
```
$>pip install -r requirements.txt
```

Install dependencies required for the unit testing and development please run
```
$>pip install -r development.txt
```

To run the application
```
$>python main.py
```

To run the tests
```
$>py.test tests.py
```


After opening [test web page](http://www.sainsburys.co.uk/webapp/wcs/stores/servlet/CategoryDisplay?listView=true&orderBy=FAVOURITES_FIRST&parent_category_rn=12518&top_category=12518&langId=44&beginIndex=0&pageSize=20&catalogId=10137&searchTerm=&categoryId=185749&listId=&storeId=10151&promotionId=#langId=44&storeId=10151&catalogId=10137&categoryId=185749&parent_category_rn=12518&top_category=12518&pageSize=20&orderBy=FAVOURITES_FIRST&searchTerm=&beginIndex=0&hideFilters=true)

one can notice that AJAX query is executed. The response of the query is a json content with a list of products in html. I used this list to parse the json, Iterate through the elements and extracting relevant data from html. Additionally each element is followed through to the product page where description and page size is being obtained. 