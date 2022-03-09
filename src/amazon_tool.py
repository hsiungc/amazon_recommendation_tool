import sys
import datafile_connect
from ProductCharac import ProdChar
from AmazonFeat import AmFeat
from Engagement import Engage
from CategoryScore import CatScor
from SummaryStats import SumStat

try:
    file_prompt = sys.argv[0]

except IndexError:
    print('Please enter the file name only')

# Open data files based on product selection
exec(open('button.py').read())

try:
    if prodchoice == 'French Press':
        data_select = datafile_connect.frenchpress_data()
    if prodchoice == 'Treadmill':
        data_select = datafile_connect.treadmill_data()
    if prodchoice == 'Wine Stopper':
        data_select = datafile_connect.winestopper_data()

    overallscore = CatScor(data_select.product_data, data_select.seller_data, data_select.review_data)
    summarystats = SumStat(data_select.product_data, data_select.seller_data, data_select.review_data)
    addstats = AmFeat(data_select.product_data)

    exec(open('report_wind.py').read())
    exec(open('summary_wind.py').read())

except:
    print('Thank you for using the Amazon BI Tool!')


