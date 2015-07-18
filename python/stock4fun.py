#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 10:56:48 2015

@author: Ken Ouyang
"""

import urllib

def stockCheck(symbol):
    if symbol.lower() == 'oil':
        base_url = 'http://www.bloomberg.com/energy/'
        content = urllib.urlopen(base_url).read()
        location = content.find("(WTI)</td>\n<td>USD/bbl.")
        [price,na,increase]=content[location:location+200]\
        .replace('\n','').replace('<td>', '|').replace('</td>','|').replace('<td class="up">','|').replace('<td class="down">','|').split('|')[4:7]
    else:
        base_url = 'http://finance.google.com/finance?q='
        content = urllib.urlopen(base_url + symbol).read()
        location = content.lower().find('values:["' + symbol + '"')
        [price,increase] = content[location:location+200].split('","')[2:4]
        increasePc = str(round(100.0*float(increase[1:])/float(price),2))+'%'
    print '%+7s %+6s (%+6s )' % (price, increase,increasePc)

#stockCheck('oil')
stockCheck('aapl')
stockCheck('msft')
stockCheck('nrg')
stockCheck('goog')
stockCheck('amzn')
stockCheck('baba')
stockCheck('lnkd')


#symbol = 'linkedin'
#base_url = 'http://finance.google.com/finance?q='
#content = urllib.urlopen(base_url + symbol).read()
#location = content.lower().find('values:["' + symbol + '"')
#content[location-50:location+50]


nrg = 26.13*90
msft = 46.01*100

