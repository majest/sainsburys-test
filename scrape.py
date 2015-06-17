import requests
from pyquery import PyQuery
import json
import sys
import hurry.filesize

class SainsburysScraper:
    
    
    def extract_products_from_list(self, url):
        """
        Retrieves the json content from online web page and attempts to parse the products.
        Each product on the json list is represented by html from which then
        individual data is extracted. Additionally it retrieves the information
        about the product itself.
        """

        print 'Please wait...'

        # get the data
        response = requests.get(url)
        content = response.content

        product_list = self.get_product_list(content)

        products = {"results" : []}

        for product_json in product_list:

            # retrieve and append the product
            products["results"].append(self.get_product(product_json['result']))
          
        self.calculate_total(products)

        return products

    def get_product_list(self, content):
        """
        Validates the product list. It assumes the input data is json
        """

        jsonData = json.loads(unicode(content, "ISO-8859-1"))

        # check if we have the products
        if 'products' not in jsonData[3]['productLists'][0]:
            raise ValueError('Invalid data. Expected products')

        # return product list
        return jsonData[3]['productLists'][0]['products']



    def get_product(self, content):
        """
        Gets the product information. It parses product html and extracts relevant information like title and price. 
        Additionally it will follow the product url and extract product description and web page size
        """

        product = {}

        # load the html
        pq = PyQuery(content)

        # clean up unit price by removing extra characters
        product['unit_price'] = float(pq('p.pricePerUnit').text().split('/')[0][1:])


        # extract product title
        product['title'] = pq('div.productInfo h3 a').text()

        # get the url to calculate the size of the product page
        url = pq('div.productInfo h3 a').attr('href')

        response = requests.get(url)
        
        # parse the product page
        pqp = PyQuery(response.content)

        # content-length header is not present in response.headers so calculating size manually with some human readable values
        product['size'] = hurry.filesize.size(len(response.content))

        # get the description
        product['description'] = pqp('div.productText p').eq(0).text()
        
        return product

    def calculate_total(self, products):
        """
        Appends total value of the items on the list. Throws an exception if list is empty
        """

        total = 0

        if len(products["results"]) == 0:
            raise ValueError('Empty product list. Can\'t calculate total value')

        for product in products["results"]:
            total += product['unit_price']

        products['total'] = total

    def format(self, data):
        print json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))

    def scrape(self, url):
        """
        Wrapper for extract_products_from_list method which will catch the exceptions and display them
        """

        try:

            self.format(self.extract_products_from_list(url))

        # Just inform there's a problem
        except Exception as e:

            print  e.message
            sys.exit(1)
