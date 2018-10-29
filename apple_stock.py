#!/usr/bin/env python
#! -*- coding: utf-8 -*-
"""IS211_Assingment09; BeautifulSoup"""

import urllib2
from bs4 import BeautifulSoup

web_page = ('http://finance.yahoo.com/q/hp?s=AAPL+Historical+Prices')
html = urllib2.urlopen(web_page)
soup = BeautifulSoup(html, 'html.parser')

s_data = soup.find_all('tr')

print 'Apple Stock'

for tr in s_data:
    for col in tr.find_all('td'):
        tds = tr.find_all("td")
        date = str(tds[0].get_text())
        close = str(tds[4].get_text())
        print ('Date: {} - Closing: {} ').format(date, close)
