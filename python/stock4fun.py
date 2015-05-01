#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 10:56:48 2015

@author: Ken Ouyang
"""

import urllib

def stockCheck(symbol):
    base_url = 'http://finance.google.com/finance?q='
    content = urllib.urlopen(base_url + symbol).read()
    location = content.lower().find('values:["' + symbol + '"')
    [price,increase] = content[location:location+200].split('","')[2:4]
    print price, increase


stockCheck('aapl')
stockCheck('nrg')
stockCheck('goog')
stockCheck('amzn')
stockCheck('baba')
stockCheck('lnkd')


#symbol = 'linkedin'
#base_url = 'http://finance.google.com/finance?q='
#ontent = urllib.urlopen(base_url + symbol).read()
#location = content.lower().find('values:["' + symbol + '"')
#content[location-50:location+50]