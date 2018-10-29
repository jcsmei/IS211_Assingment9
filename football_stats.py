#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211_Assingment09; A simple web scraping app with BeautifulSoup."""

import urllib2
from bs4 import BeautifulSoup

web_page = ('https://www.cbssports.com/nfl/stats/'
            'playersort/nfl/year-2018-season-regular-category-touchdowns')

html = urllib2.urlopen(web_page)
soup = BeautifulSoup(html, 'html.parser')
td_table = soup.findAll(
    'table', attrs={'class':'data'})[0].findAll(
        'tr', attrs={'valign':'top'})

def main():
    counter = 0
    for i in td_table:
        name = i.findAll('td')[0].findAll('a')[0].contents[0]
        position = i.findAll('td')[1].contents[0]
        team =  i.findAll('td')[2].findAll('a')[0].contents[0]
        tds = i.findAll('td')[6].contents[0]
        counter += 1
        if counter == 1:
            print ('-Top 20 Players with The Most Touchdowns-\n'
                   '-----------------------------------------\n'
                   '| No.| Player       | Position | Team | TD |\n'
                   '--------------------------------------------\n'
                   '| {} | {}   | {}      | {}    | {}').format(counter,
                                                                name, 
                                                                position, 
                                                                team, 
                                                                tds)
        elif counter >= 1 and counter <=20:
            print ("| {} | {}   | {}    | {}      | {}").format(counter,
                                                                name,
                                                                position,
                                                                team,
                                                                tds)
        if counter >= 20:
            break
            
if __name__ == '__main__':
    main()
