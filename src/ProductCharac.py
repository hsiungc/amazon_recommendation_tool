import re

class ProdChar():
    '''Class to gather and organize Amazon product characteristics data'''
    
    def __init__(self,proddata, sellerdata):
        self.proddata = proddata
        self.sellerdata = sellerdata
        self.prod_name = []
        self.prod_price = []
        self.prod_weight = []
        self.prod_size = []
        self.prod_material = []
        self.prod_seller = []
        self.seller_avg = []
        self.seller_rate = []
    
    def data_len(self):
        return len(self.proddata['prod'])
    
    def get_prod_name(self):
        '''Append all product names into list, count total names'''
        classlist = []
        count = 0
        
        for item in self.proddata['prod']:
            if 'name' in item:
                classlist += item['name']
                self.prod_name.append(''.join(classlist))
                classlist = []
                count += 1
                
        return self.prod_name
        
    def get_prod_price(self):
        '''Append sell prices for all products into list'''
        classlist = []
        prices = []
        count = 0
        
        # Retrieve price list
        for item in self.proddata['prod']:
            if 'sellprice' in item:
                classlist += item['sellprice']
                prices.append(''.join(classlist))
                classlist = []
                count += 1
        
        # Convert prices to numerical values
        for strings in prices:
            dollar = strings[1:]
            dollar = dollar.replace(',','')
            convt = float(dollar)
            self.prod_price.append(convt)

        return self.prod_price
        
    def get_prod_weight(self):
        '''Append product weights for all products into list'''
        classlist = []
        weightlist = []
        count = 0
        lbconv = []
        lbstr = ''
        ozconv = []
        ozstr = ''

        # Create list of product weights
        for item in self.proddata['prod']:
            if 'weight' in item:
                classlist += item['weight']
                weightlist.append(''.join(classlist))
                classlist = []
                count += 1

        # Keep only numeric values in list
        for we in weightlist:
            
            # Gather list of pound units
            if 'pound' in we.lower():
                if '.' in we.lower():
                    lbconv += re.findall("\d+\.\d+", we)
                else:
                    for lbint in we:
                        if lbint.isdigit():
                            lbstr += lbint
                    lbconv.append(lbstr)
                    lbstr = ''

            # Gather list of ounce units
            if 'ounce' in we.lower():
                if '.' in we.lower():
                    ozconv += re.findall("\d+\.\d+", we)
                else:
                    for ozint in we:
                        if ozint.isdigit():
                            ozstr += ozint
                    ozconv.append(ozstr)
                    ozstr = ''

        # Convert pounds and ounces into floats, convert ounces into pounds
        for lb in lbconv:
            finallb = float(lb)
            self.prod_weight.append(finallb)

        for oz in ozconv:
            pounds = round(float(oz) * 0.0625,2)
            self.prod_weight.append(pounds)
                
        return self.prod_weight
        
    def get_prod_size(self):
        '''Calculate and append product size (l*w*h) for all products into list'''
        classlist = []
        numconv = []
        dimenconv = []
        floatconv = []
        mult = 1
        count = 0

        # Create list of product dimensions
        for item in self.proddata['prod']:
            if 'size' in item:
                classlist += item['size']
                numconv.append(''.join(classlist))
                classlist = []

        # Convert dimensions to l*w*h values
        for dimen in numconv:
            dimenconv.append(dimen.split(' i')[0])

        for inch in dimenconv:
            size = inch.split(' x ')
            if len(size) > 2:
                floatconv.append(size) 

        for vol in floatconv:
            for flt in vol:
                conv = float(flt)
                mult *= round(conv, 2)
            self.prod_size.append(round(mult, 2))
            mult = 1
        
        return self.prod_size
        
    def get_prod_material(self):
        '''Append product materials for all products into list'''
        classlist = []
        capitallet = []
        count = 0
        
        for item in self.proddata['prod']:
            if 'material' in item:
                classlist += item['material'].lower()
                capitallet.append(''.join(classlist))
                classlist = []
                count += 1
        
        for word in capitallet:
            word2 = word.title()
            self.prod_material.append(word2)
        
        return self.prod_material

    def get_prod_seller(self):
        '''Append seller names for all products into list, count total sellers'''
        classlist = []
        count = 0

        for item in self.sellerdata['prod']:
            if 'sellname' in item:
                classlist += item['sellname']
                self.prod_seller.append(''.join(classlist))
                classlist = []
                count += 1

        return self.prod_seller
        
    def get_seller_avg(self):
        '''Append seller feedback ratings into list'''
        classlist = []
        numconv = []
        count = 0

        for item in self.sellerdata['prod']:
            if 'positive' in item:
                classlist += item['positive']
                numconv.append(''.join(classlist))
                classlist = []
                count += 1
                
        for num in numconv:
            perc = num.replace('%','')
            flrate = float(perc)
            self.seller_avg.append(flrate)
        
        return self.seller_avg
        
    def get_seller_rate(self):
        '''Append seller # of ratings into list'''
        classlist = []
        compilelist = []
        count = 0


        for item in self.sellerdata['prod']:
            if 'sell_ratings' in item:
                classlist += re.findall("\(+\d+", item['sell_ratings'])
                compilelist.append(''.join(classlist))
                classlist = []
                count += 1

        for ratings in compilelist:
            ratings = ratings.replace('(','')
            ratings = int(ratings)
            self.seller_rate.append(ratings)
            
        return self.seller_rate 
