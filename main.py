# Author: Warren Liu
# Date: 5/17/2021
# First web crawler project
# Project: Web crawler from Letto website
#          get data for trainning AI
#
# Version 0.1

from typing import List
import requests
from bs4 import BeautifulSoup
from datetime import *
from dateutil import parser
import csv

PATH = './data/'
url_base = r'https://www.lottoamerica.com/powerball/archive/'
year_base = ['2021','2020','2019','2018','2017','2016','2015','2014','2013',
             '2012','2011','2010','2009','2008','2007','2006','2005','2004',
             '2003','2002','2001','2000','1999','1998','1997','1996','1995',
             '1994','1993','1992']


# function to get the url and the status code
#   status_code = 200 if success
def open_url(url: str):
    r = requests.get(url)
    return [r.content, r.status_code]


# function to make requests to soup content
def make_soup(content: requests.models.Response):
    soup = BeautifulSoup(content, 'lxml')
    return soup


# Letto website stores the numbers and dates in the following format:
#   <div class = "row">
#       <...>
#           <div class = "_date -sm">...</div>
#               <strong>month date</strong>
#               ", year"
#           <div class = "_date -sm">...</div>
#              <ul class = "balls -sm">...</div>
#                   <li>number1</li>
#                   <li>number2</li>
#                   <...>

# funtion to get all numbers
# Each date has 7 numbers (5 normal number + 1 bouns number + multiple power)
#   year 2000/3/7 and under do not have multiple power number
#   thus, year 2000/3/3 - 1992 only have 6 numbers
def get_numbers(soup) -> List[str]:
    num_list = []
    num_tag = soup.find_all('ul', attrs = {'class': 'balls -sm'})
    for tag in num_tag:
        tag_list = tag.find_all('li')
        for tag in tag_list:
            num_list.append(tag.string)
    return num_list


# function to get all dates
def get_dates(soup, year: str) -> List[str]:
    dates_list = []
    date_tag = soup.find_all('div', attrs = {'class': '_date -sm'})
    for tag in date_tag:
        d_list = tag.find_all('strong')
        for date in d_list:
            dates_list.append(date.string)

    return_list = []
    for day in dates_list:
        return_list.append(parser.parse(day + " " + year).strftime('%Y %m %d'))
    
    return return_list

# function to write date_list and number_list to file
def write_content(num_list, date_list, year):
    f = open(PATH + year + '.csv', 'w')
    size = len(date_list)
    for i in range(size):
        f.writelines(date_list[i] + ' ')
        for j in range(7):
            f.writelines(num_list[i * 7 + j] + ' ')
        f.write('\n')



def main():
    for i in range(21):
        # open url
        url = url_base + year_base[i]
        [content, code] = open_url(url)
        # check if open successfully
        if code != 200: raise ValueError(r'status code is {c}, open url failed.'.format(c=code))
        else: print('Open url {s} success'.format(s=url))
        # make the soup
        soup = make_soup(content)

        # get all dates and numbers
        num_list = []
        date_list = []
        num_list = get_numbers(soup)
        date_list = get_dates(soup, year_base[i])
        # check if the number of elements are correct
        if len(num_list) != len(date_list) * 7:
            raise ValueError(r'Dates count and number counts are not match. number: {n}, date: {d}'.format(n=len(num_list), d=len(date_list)))
        else: print('Successfully get dates and numbers')
        # start write to file
        print('Now write year {y} to file {f}'.format(y = year_base[i], f = year_base[i] + '.csv'))
        write_content(num_list, date_list, year_base[i])
    

if __name__ == "__main__":
    main()