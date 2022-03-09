import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Files for comparing keywords with reviews
with open("../txt/positivekw.txt","r") as poskw_load:
    raw_input1 = poskw_load.readlines()
    pos_kw = [datum.strip('\n') for datum in raw_input1]
poskw_load.close()

with open("../txt/negativekw.txt","r") as negkw_load:
    raw_input2 = negkw_load.readlines()
    neg_kw = [datum.strip('\n') for datum in raw_input2]
negkw_load.close()


class Engage():
    '''Class to gather and organize Amazon product engagement data'''
    
    def __init__(self, proddata, revdata):
        self.proddata = proddata
        self.revdata = revdata
        self.avg_rating = []
        self.num_review = []
        self.tot_reviews = []
        self.neg_keyw = []
        self.pos_keyw = []
        self.do_better = []
        
    def data_len(self):
        return len(self.proddata['prod'])
       
    def get_avg_rating(self):
        '''Append average reviews for all products into list'''
        classlist = []
        count = 0
        ratelist = []
        avg_calc = []

        for item in self.proddata['prod']:
            if 'cust_stars' in item:
                classlist += re.findall("\d+\.\d+", item['cust_stars'][0:3])
                ratelist.append(''.join(classlist))
                classlist = []
                count += 1

        for rev in ratelist:
            rev = float(rev)
            self.avg_rating.append(rev)

        return self.avg_rating
    
    def get_num_review(self):
        '''Append number reviews for each product into list'''
        classlist = []
        count = 0
        reviewlist = []

        for item in self.proddata['prod']:
            if 'reviews' in item:
                classlist += item['reviews']
                reviewlist.append(''.join(classlist))
                classlist = []
                count += 1
        
        for rev in reviewlist:
            num = rev.replace(',','')
            num = float(num)
            self.num_review.append(num)

        return self.num_review
        
    def get_reviews(self):
        '''Create list of all product reviews'''
        count = 0
        
        for item in self.revdata['prod']:
            if 'rev_det' in item:
                self.tot_reviews += item['rev_det']
                count += 1
                
        return self.tot_reviews

    def get_neg_keyw(self):
        '''Negative review keywords and word counts'''
        classlist = []
        combine = ''
        negdict = {}

        
        for item in self.revdata['prod']:
            if 'rev_det' in item:
                classlist += item['rev_det']

        reviewlist = [dict['name'] for dict in classlist if classlist]

        for rev in reviewlist:
            combine += rev.lower()

        for neg in neg_kw:
            negative = re.compile(r'(?<![^\W_]){}(?![^\W_])'.format(re.escape(neg)))
            words = negative.findall(combine)
            negdict[neg] = len(words)

        tuples = sorted(negdict.items(), key=lambda x:x[1], reverse = True)
        conv = dict(tuples)

        self.neg_keyw = (f'''{list(conv.keys())[0]} : {list(conv.values())[0]:,}\n'''
                        f'''{list(conv.keys())[1]} : {list(conv.values())[1]:,}\n'''
                        f'''{list(conv.keys())[2]} : {list(conv.values())[2]:,}\n'''
                        f'''{list(conv.keys())[3]} : {list(conv.values())[3]:,}\n'''
                        f'''{list(conv.keys())[4]} : {list(conv.values())[4]:,}''')

        return self.neg_keyw
        
    def get_pos_keyw(self):
        '''Positive review keywords and word counts'''
        classlist = []
        combine = ''
        posdict = {}
        count = 0

        for item in self.revdata['prod']:
            if 'rev_det' in item:
                classlist += item['rev_det']
                count += 1

        reviewlist = [dict['name'] for dict in classlist if classlist]

        for rev in reviewlist:
            combine += rev.lower()

        for pos in pos_kw:
            positive = re.compile(r'(?<![^\W_]){}(?![^\W_])'.format(re.escape(pos)))
            words = positive.findall(combine)
            posdict[pos] = len(words)

        tuples = sorted(posdict.items(), key=lambda x:x[1], reverse = True)
        conv = dict(tuples)

        self.pos_keyw = (f'''{list(conv.keys())[0]} : {list(conv.values())[0]:,}\n'''
                        f'''{list(conv.keys())[1]} : {list(conv.values())[1]:,}\n'''
                        f'''{list(conv.keys())[2]} : {list(conv.values())[2]:,}\n'''
                        f'''{list(conv.keys())[3]} : {list(conv.values())[3]:,}\n'''
                        f'''{list(conv.keys())[4]} : {list(conv.values())[4]:,}''')
        
        return self.pos_keyw
    
    def get_do_better(self):
        '''Review keywords to help improve product'''
        combine = ''
        classlist = []
        checker = []

        for item in self.revdata['prod']:
            if 'rev_det' in item:
                classlist += item['rev_det']

        reviewlist = [dict['name'] for dict in classlist if classlist]
        sample = reviewlist[:100]

        for rev in sample:
            for neg in neg_kw:
                if neg in rev.split():
                    combine += rev.lower()

        keywords = set(stopwords.words('english'))
        reviewords = word_tokenize(combine)
        wordtable = dict()

        for word in reviewords:
            word = word.lower()
            if word in keywords:
                continue
            if word in wordtable:
                wordtable[word] += 1
            else:
                wordtable[word] = 1

        revsent = sent_tokenize(combine)
        senttable = dict()

        for sentence in revsent:
            for word, num in wordtable.items():
                if word in sentence.lower():
                    if sentence in senttable:
                        senttable[sentence] += num
                    else:
                        senttable[sentence] = num


        sumValues = 0
        for sentence in senttable:
            sumValues += senttable[sentence]

            
        average = int(sumValues / len(senttable))

        summ = ''
        for sentence in revsent:
            if (sentence in senttable) and (senttable[sentence] > (1.2 * average)):
                summ += " " + sentence
                
        sentlist = summ.split('.')

        for sent in sentlist:
            sent = sent.strip().capitalize()
            if sent in checker or len(sent) <= 10:
                continue
            else:
                checker.append(sent)


        self.do_better = (f''' - {checker[0]}\n'''
                        f''' - {checker[1]}\n'''
                        f''' - {checker[2]}\n'''
                        f''' - {checker[3]}\n'''
                        f''' - {checker[4]}''')

        return self.do_better
