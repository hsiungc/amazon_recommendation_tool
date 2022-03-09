with open("../txt/amazon_bsr_list.txt","r") as bsr_load:
    raw_input4 = bsr_load.readlines()
    bsr_list = [datum.strip('\n') for datum in raw_input4]
bsr_load.close()


class AmFeat():
    '''Class to gather and organize Amazon features data'''
    
    def __init__(self, proddata):
        self.proddata = proddata
        self.amaz_choice = []
        self.amaz_brand = 0
        self.prod_bsr = []
        self.bsr_calc = 0
        self.total_best_sell = []
        self.best_sell_cate = []
        self.fulfill_type = []
        self.prime = []
        
    def data_len(self):
        return len(self.proddata['prod'])        
    
    def get_amaz_choice(self):
        '''Count # of Amazon Choice products'''
        classlist = []
        count = 0

        for item in self.proddata['prod']:
            if 'amazchoice' in item:
                classlist += item['amazchoice']
                self.amaz_choice.append(''.join(classlist))
                classlist = []
                count += 1
        
        return len(self.amaz_choice)
    
    def get_amaz_brand(self):
        '''Count # of Amazon Brand products, based on keywords (Basics, Essentials)'''
        classlist = []
        count = 0
        amazlist = []

        for item in self.proddata['prod']:
            if 'sold_type' in item:
                classlist += item['sold_type']
                amazlist.append(''.join(classlist))
                classlist = []
                count += 1

        for value in amazlist:        
            if 'Amazon' in value:
                self.amaz_brand += 1

        return self.amaz_brand

    def get_bsr(self):
        '''Retrieve all BSR ratings'''
        classlist = []
        count = 0
        numbers = []
        ranklist = []

        for item in self.proddata['prod']:
            if 'bsr' in item:
                for rank in item['bsr'][1:10]:
                    if rank.isnumeric():
                        classlist += rank
                        numbers.append(''.join(classlist))
                        classlist = []

                    else:
                        rank.replace(',','')

                ranklist.append(''.join(numbers))
                numbers = []
                count += 1
                
            for ranking in ranklist:
                proper_rank = int(ranking)
                self.prod_bsr.append(proper_rank)
                
            return self.prod_bsr
        
    def get_bsr_calc(self):
        '''Retrieve best BSR rankings under 5,000'''
        classlist = []
        count = 0
        numbers = []
        ranklist = []

        for item in self.proddata['prod']:
            if 'bsr' in item:
                for rank in item['bsr'][1:10]:
                    if rank.isnumeric():
                        classlist += rank
                        numbers.append(''.join(classlist))
                        classlist = []

                    else:
                        rank.replace(',','')

                ranklist.append(''.join(numbers))
                numbers = []
                count += 1

        for ranking in ranklist:
            proper_rank = int(ranking)
            if proper_rank <= 5000:
                self.bsr_calc += 1
             
        return self.bsr_calc 
        
    def get_total_best_sell(self):
        classlist = []
        count = 0
        numbers = []
        ranklist = []

        for item in self.proddata['prod']:
            if 'bsr' in item:
                for rank in item['bsr'][1:10]:
                    if rank.isnumeric():
                        classlist += rank
                        numbers.append(''.join(classlist))
                        classlist = []

                    else:
                        rank.replace(',','')

                ranklist.append(''.join(numbers))
                numbers = []
                count += 1

        firstcount = 0        
        secondcount = 0        
        thirdcount = 0        
        fourthcount = 0
        fifthcount = 0
        sixthcount = 0

        for ranking in ranklist:
            proper_rank = int(ranking)
            if proper_rank <= 100:
                firstcount += 1
            if proper_rank <= 500:
                secondcount += 1
            if proper_rank <= 1000:
                thirdcount += 1
            if proper_rank <= 5000:
                fourthcount += 1
            if proper_rank <= 10000:
                fifthcount += 1
            if proper_rank <= 50000:
                sixthcount += 1

        self.total_best_sell = (f'''Rankings above 100: {firstcount}\n'''
                                f'''Rankings above 500: {secondcount}\n'''
                                f'''Rankings above 1,000: {thirdcount}\n'''
                                f'''Rankings above 5,000: {fourthcount}\n'''
                                f'''Rankings above 10,000: {fifthcount}\n'''
                                f'''Rankings above 50,000: {sixthcount}\n''' 
                                f'''Total Rankings: {len(ranklist)}''')
        
        return self.total_best_sell

    def get_best_sell_cate(self):
        classlist = []
        count = 0
        categories = []
        countslist = []

        for item in self.proddata['prod']:
            if 'bsr' in item:
                classlist += item['bsr']
                categories.append(''.join(classlist))
                classlist = []
                count += 1

        for rank in bsr_list:
            for item in categories:
                if rank in item:
                    countslist.append(rank)

        self.best_sell_cate = {ranks : countslist.count(ranks) for ranks in countslist}

        return self.best_sell_cate
        
    def get_fulfill_type(self):
        '''Count # of FBA and FBM products'''
        classlist = []
        count = 0
        
        for item in self.proddata['prod']:
            if 'ship_type' in item:
                classlist += item['ship_type']
                self.fulfill_type.append(''.join(classlist))
                classlist = []
                count += 1

            return self.fulfill_type
            
    def get_prime(self):
        '''Count number of Prime products'''
        classlist = []
        count = 0

        for item in self.proddata['prod']:
            if 'amazprime' in item:
                classlist += item['amazprime']
                self.prime.append(''.join(classlist))
                classlist = []
                count += 1

        return len(self.prime)
