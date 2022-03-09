import statistics
from ProductCharac import ProdChar
from AmazonFeat import AmFeat
from Engagement import Engage

class CatScor(ProdChar, Engage, AmFeat):
    '''Class to assign weight to attributes and calculate product score'''    
    
    def __init__(self, proddata, sellerdata, revdata):
        ProdChar.__init__(self, proddata, sellerdata)
        Engage.__init__(self, proddata, revdata)
        AmFeat.__init__(self, proddata)
        self.proddata = proddata
        self.sellerdata = sellerdata
        self.revdata = revdata
        self.pricew = 0.35
        self.weightw = 0.35
        self.sizew = 0.3
        self.bsrw = 0.2
        self.revnumw = 0.25
        self.starsw = 0.25
        self.sellerw = 0.15
        self.amazbrandw = 0.15
    
    def price_score(self):
        '''Retrieve price information and assign score'''
        
        # Calculate average price
        avgprice = statistics.mean(self.get_prod_price())
        
        # Score average price
        if(avgprice > 30 and avgprice <= 45):
            price_scor = 5        
        if(avgprice > 20 and avgprice <= 30) or (avgprice > 45 and avgprice <= 55):
            price_scor = 4        
        if(avgprice > 12 and avgprice <= 20) or (avgprice > 55 and avgprice <= 65):
            price_scor = 3        
        if (avgprice > 5 and avgprice <= 12) or (avgprice > 65 and avgprice <= 75):
            price_scor = 2        
        if avgprice <= 5 or avgprice > 75:
            price_scor = 1

        return price_scor
        
    def weight_score(self):
        '''Retrieve weight information and assign score'''
        
        # Calculate average weight
        avgweight = statistics.mean(self.get_prod_weight())
    
        # Score average weight
        if avgweight <= 2:
            weight_scor = 5
        if 2 < avgweight <= 5:
            weight_scor = 4
        if 5 < avgweight <= 8:
            weight_scor = 3
        if 8 < avgweight <= 12:
            weight_scor = 2
        if avgweight > 12:
            weight_scor = 1        
        
        return weight_scor
    
    def size_score(self):
        '''Retrieve size information and assign score'''
    
        # Calculate average volume
        avgsize = statistics.mean(self.get_prod_size())
        
        # Score average volume (cubic inches)
        if avgsize <= 500:
            size_scor = 5
        if avgsize > 500 and avgsize <= 700:
            size_scor = 4
        if avgsize > 700 and avgsize <= 1100:
            size_scor = 3
        if avgsize > 1100 and avgsize <= 2000:
            size_scor = 2
        if avgsize > 2000:
            size_scor = 1        
        
        return size_scor
        
    def bsr_score(self):
        '''Retrieve BSR information and assign score'''
        
        # Calculate strength based on # best seller rankings below 5,000
        bsrstrgth = self.get_bsr_calc()/len(self.get_bsr())
        
        # Score bsr strength
        if bsrstrgth <= 0.04:
            bsr_scor = 5
        if bsrstrgth > 0.04 and bsrstrgth <= 0.08:
            bsr_scor = 4
        if bsrstrgth > 0.08 and bsrstrgth <= 0.1:
            bsr_scor = 3
        if bsrstrgth > 0.1 and bsrstrgth <= 0.12:
            bsr_scor = 2
        if bsrstrgth > 0.12:
            bsr_scor = 1

        return bsr_scor
    
    def rev_compare_score(self):
        '''Retrieve total review information and assign score'''
        avglist = []
        
        # Calculate average # of reviews for top 10 products
        for revs in self.get_num_review()[:10]:
            avglist.append(revs)
        
        avgcalc = statistics.mean(avglist)
        
        # Score the average # of reviews
        if avgcalc <= 150:
            rev_scor = 5
        if avgcalc > 150 and avgcalc <= 500:
            rev_scor = 4
        if avgcalc > 500 and avgcalc <= 1000:
            rev_scor = 3
        if avgcalc > 1500 and avgcalc <= 5000:
            rev_scor = 2
        if avgcalc > 5000:
            rev_scor = 1

        return rev_scor
    
    def rev_stars_score(self):
        '''Retrieve average product review ratings and asign score'''
        
        # Calculate average review stars
        staravg = statistics.mean(self.get_avg_rating())
            
        if staravg <= 3.5:
            star_scor = 5
        if staravg > 3.5 and staravg <= 4.0:
            star_scor = 4
        if staravg > 4.0 and staravg <= 4.5:
            star_scor = 3
        if staravg > 4.5 and staravg <= 4.8:
            star_scor = 4
        if staravg > 4.8:
            star_scor = 5

        return star_scor
    
    def seller_score(self):
        '''Retrieve Amazon seller feedback ratings and assign score'''
        
        # Calculate average seller rating
        avgsell = statistics.mean(self.get_seller_avg())
        
        # Score average seller rating
        if avgsell <= 0.8:
            sell_scor = 5
        if avgsell > 0.8 and avgsell <= 0.87:
            sell_scor = 4
        if avgsell > 0.87 and avgsell <= 0.93:
            sell_scor = 3
        if avgsell > 0.93 and avgsell <= 0.98:
            sell_scor = 2
        if avgsell > 0.98:
            sell_scor = 1
        
        return sell_scor
    
    def amazbrand_score(self):
        '''Retrieve Amazon brand information and assign score'''

        # Calculate # products sold by Amazon
        brandcalc = self.get_amaz_brand()/self.data_len()
        
        # Score Amazon brand %
        if brandcalc <= 0.01:
            brand_scor = 5
        if brandcalc > 0.01 and brandcalc <= 0.03:
            brand_scor = 4
        if brandcalc > 0.03 and brandcalc <= 0.05:
            brand_scor = 3
        if brandcalc > 0.05 and brandcalc <= 0.08:
            brand_scor = 2
        if brandcalc > 0.08:
            brand_scor = 1

        return brand_scor
    
    def logist_cat_score(self):
        '''Assign weighting and calculate score for logistical category'''
        price = self.price_score() * self.pricew
        weight = self.weight_score() * self.weightw
        size = self.size_score() * self.sizew
        
        # Sum individual scores and multiply by 2 to scale from 1-10
        logist_scor = round((price + weight + size) * 2, 2)
    
        return logist_scor
    
    def comp_cat_score(self):
        '''Assign weighting and calculate score for competitive marketplace category'''
        bsr = self.bsr_score() * self.bsrw
        review = self.rev_compare_score() * self.revnumw
        stars = self.rev_stars_score() * self.starsw
        seller = self.seller_score() * self.sellerw
        amazbrand = self.amazbrand_score() * self.amazbrandw        
    
        # Sum individual scores and multiply by 2 to scale from 1-10
        comp_scor = round((bsr + review + stars + seller + amazbrand) * 2, 2)
    
        return comp_scor
        
    def calculate_final_score(self):
        '''Calculate overall final product score'''

        # Sum category scores and divide by 2
        final_scor = round((self.logist_cat_score()+ self.comp_cat_score()) / 2, 1)
        
        return final_scor
