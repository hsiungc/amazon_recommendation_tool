# OPEN DATA FILES

import json

# File loads need to be created for each product

class frenchpress_data:
    def __init__(self):
        with open('../data/fp_attrib.json', 'r') as data_load:
            self.product_data = json.load(data_load)
        data_load.close()

        with open('../data/fp_seller.json', 'r') as seller_load:
            self.seller_data = json.load(seller_load)
        seller_load.close()

        with open('../data/fp_reviews.json', 'r') as review_load:
            self.review_data = json.load(review_load)
        review_load.close()

class treadmill_data:
    def __init__(self):
        with open('../data/treadmill_attrib.json', 'r') as data_load:
            self.product_data = json.load(data_load)
        data_load.close()

        with open('../data/treadmill_seller.json', 'r') as seller_load:
            self.seller_data = json.load(seller_load)
        seller_load.close()

        with open('../data/treadmill_reviews.json', 'r') as review_load:
            self.review_data = json.load(review_load)
        review_load.close()
    
class winestopper_data:
    def __init__(self):
        with open('../data/wine_attrib.json', 'r') as data_load:
            self.product_data = json.load(data_load)
        data_load.close()

        with open('../data/wine_seller.json', 'r') as seller_load:
            self.seller_data = json.load(seller_load)
        seller_load.close()

        with open('../data/wine_reviews.json', 'r') as review_load:
            self.review_data = json.load(review_load)
        review_load.close()
