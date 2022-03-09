import statistics
from ProductCharac import ProdChar
from AmazonFeat import AmFeat
from Engagement import Engage


class SumStat(ProdChar, Engage, AmFeat):
    
    def __init__(self, proddata, sellerdata, revdata):
        ProdChar.__init__(self, proddata, sellerdata)
        Engage.__init__(self, proddata, revdata)
        AmFeat.__init__(self, proddata)
        self.proddata = proddata
        self.sellerdata = sellerdata
        self.revdata = revdata
    
    def price_range(self):
        '''Retrieve prod_price list from ProdChar, calculate max and min'''
        maxprice = max(self.get_prod_price())
        minprice = min(self.get_prod_price())
        
        return f'${minprice:,.2f} - ${maxprice:,.2f}'
        
    def price_median(self):
        '''Retrieve prod_price list from ProdChar, calculate median'''
        medprice = statistics.median(self.get_prod_price())
    
        return f'${medprice:,}'
    
    def top_prod_avgrev(self):
        '''Sum total number of reviews from num_review '''
        avglist = []
        
        # Calculate average # of reviews for top 10 products
        for revs in self.get_num_review()[:10]:
            avglist.append(revs)
        
        avgcalc = statistics.mean(avglist)
        
        return f'{int(avgcalc):,}'
        
    def get_sum_negkw(self):
        '''Display negative keywords with most counts'''

        # Print top 10 words and word count from reviews
        return self.get_neg_keyw()
        
    def get_sum_poskw(self):
        '''Display positive keywords with most counts'''

        # Print top 10 words and word count from reviews
        return self.get_pos_keyw()
    
    def get_sum_dobet(self):
        '''Display keywords to help improve product'''
            
        # Print top 10 words and word count
        return self.get_do_better()

    def overall_rating(self):
        '''Retrieve avg_rating from Engage, calculate average'''
        avgstars = statistics.mean(self.get_avg_rating())
        
        return f'{avgstars:.1f} out of 5.0 stars'
    
    def sellertype(self):
        '''Distinguish between Amazon brand vs. third party/vendor'''
        percentage = self.get_amaz_brand()/self.data_len()
        
        return '{:.2%}'.format(percentage)
