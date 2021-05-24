# -*- coding:utf-8 -*-
# Author: Warren Liu
# Date: 5/21/2021
# Project: Analyze the Powerball data
#
# Write to file format:
#   Top N numbers, follow by each number's show-up time
#   e.g. 1 2 3 4 5 6 100 90 80 70 60 50
#           ||          ||
#       [ Top 6 num ][each num show-up time]
#   this number's shop-up time = this number's index + TOP_N (pre-defined int)

from collections import Counter
import os
import datetime
from datetime import date, timedelta
from tqdm import tqdm
import calendar

SRC_PATH = './data/merged_file/'
OUT_PATH = './data/analyzed_data/'
ALL_YEAR_PATH = './data/all_years/'
no_year_file = SRC_PATH + 'merged_file_without_year.csv'
no_date_file = SRC_PATH + 'merged_file_without_date.csv'
year_file = SRC_PATH + 'merged_file.csv'
final_file_path = './data/conclusion/'

TOP_N = 10
GENERATED_FILE_NUM = 4
FACTOR = 0.25


# function to write each x's top numbers to a file
def each_x_top():
    fin = open(no_year_file)
    num_month = []
    num_date = []

    for _ in range (12):
        num_month.append([])
    for _ in range(31):
        num_date.append([])

    for l in tqdm(fin.readlines()):
        l = l.split(' ')
        # get top n of each month
        for month in range (1, 13):
            if l[0] == ('0' + str(month) if month < 10 else str(month)):
                for i in range(6):
                    num_month[month - 1].append(l[2 + i])
        # get top n of each date
        for date in range(1, 32):
            if l[1] == ('0' + str(date) if date < 10 else str(date)):
                for i in range (6):
                    num_date[date - 1].append(l[2 + i])
    fin.close()

    if not os.path.exists(OUT_PATH):
        os.mkdir(OUT_PATH)
    # write top n of each month to a file
    f = open(OUT_PATH + 'm_top_num_list.csv', 'w')
    for i in range(12):
        f.writelines(number + ' ' for (number, _) in Counter(num_month[i]).most_common(TOP_N))
        f.writelines(str(cnt) + ' ' for (_, cnt) in Counter(num_month[i]).most_common(TOP_N))
        f.write('\n')
    f.close()
    # write top n of each date to a file
    f = open(OUT_PATH + 'd_top_num_list.csv', 'w')
    for i in range (31):
        #print(Counter(num_date[i]).most_common(6))
        f.writelines(number + ' ' for (number, _) in Counter(num_date[i]).most_common(TOP_N))
        f.writelines(str(cnt) + ' ' for (_, cnt) in Counter(num_date[i]).most_common(TOP_N))
        f.write('\n')
    f.close()


# function to get each weekday's top n
def each_weekday_top():
    fin = open(year_file)
    num = []
    for _ in range(7):
        num.append([])
    
    for l in tqdm(fin.readlines()):
        l = l.split(' ')
        # convert date into weekday
        this_weekday = datetime.datetime(int(l[0]), int(l[1]), int(l[2])).weekday()
        for weekday in range(7):
            if this_weekday == weekday:
                for i in range(6):
                    num[weekday].append(l[3 + i])
    fin.close()

    # write
    f = open(OUT_PATH + 'wd_top_num_list.csv', 'w')
    for i in range(7):
        f.writelines(number + ' ' for (number, _) in Counter(num[i]).most_common(TOP_N))
        #f.write('\n')
        f.writelines(str(cnt) + ' ' for (_, cnt) in Counter(num[i]).most_common(TOP_N))
        f.write('\n')
    f.close()


# function to get the top n number of:
#   if this number occurs
#   what numbers will show up in the next game
def this_num_next_top():
    f = open(OUT_PATH + 'next_top_num_list.csv', 'w')
    for i in tqdm(range(68)):
        num = i + 1
        fin = open(no_date_file)
        num_list = []

        save = False
        for l in fin.readlines():
            l = l.split(' ')
            # if this line need to be saved, save, and set save to false
            if save is True:
                for numbers in l[1:-1]:
                    num_list.append(numbers)
                save = False
            # if this line contains the numbers we are looking for, save the next line
            if any(numbers == str(num) for numbers in l): save = True
        fin.close()
    
        # write
        
        f.writelines(number + ' ' for (number, _) in Counter(num_list).most_common(TOP_N))
        f.writelines(str(cnt) + ' ' for (_, cnt) in Counter(num_list).most_common(TOP_N))
        f.write('\n')
    f.close()


def get_each_top():
    each_x_top()
    each_weekday_top()
    this_num_next_top()


# function to calculate the most possible show up number
def get_most_possible_num():

    input_file_src = OUT_PATH
    today = datetime.datetime.today()
    year = today.year
    month = today.month
    day = today.day
    weekday = datetime.datetime(year, month, day).weekday()
    print('You are asking for date {}/{}/{}, {}'.format(year, month, day, calendar.day_name[weekday]))

    # get the next Powerball date if current date is not Powerdate date
    next = 0
    if weekday != 2 and weekday != 5:
        if weekday >= 0 and weekday <= 2:
            weekday = 2
            next = 2 - weekday
        else:
            weekday = 5
            if weekday < 5:
                next = 5 - weekday
            else:
                next = 6 - weekday + 2
        # uodate date
        today += datetime.timedelta(days=next)
        year = today.year
        month = today.month
        day = today.day
        weekday = datetime.datetime(year, month, day).weekday()
        print('Today is not a Powerball day, now displaying info for {}/{}/{}, {}'.format(year, month, day, calendar.day_name[weekday]))

    # get the month_top_n, date_top_n, weekday_top_n, next_top, and last winning number list
    month_list = []
    date_list = []
    wd_list = []
    last_win = []
    next_list = []
    # month top
    fin = open(input_file_src + 'm_top_num_list.csv', 'r')
    line_cnt = 0
    for line in fin.readlines():
        if line_cnt + 1 == month:
            line = line.split(' ')
            for i in range(TOP_N * 2):
                month_list.append(line[i])
            break
        line_cnt += 1
    fin.close()
    # date top
    fin = open(input_file_src + 'd_top_num_list.csv', 'r')
    line_cnt = 0
    for line in fin.readlines():
        if line_cnt + 1 == day:
            line = line.split(' ')
            for i in range(TOP_N * 2):
                date_list.append(line[i])
            break    
        line_cnt += 1
    fin.close()
    # weekday top
    fin = open(input_file_src + 'wd_top_num_list.csv', 'r')
    line_cnt = 0
    for line in fin.readlines():
        if line_cnt == weekday:
            line = line.split(' ')
            for i in range(TOP_N * 2):
                wd_list.append(line[i])
            break    
        line_cnt += 1
    fin.close()
    # last win
    fin = open(ALL_YEAR_PATH + str(year) + '.csv')
    for line in fin.readlines():
        line = line.split(' ')
        for i in range(9):
            if i > 2:
                last_win.append(line[i])
        break
    last_win = [int(num) for num in last_win]
    last_win.sort()
    # next top
    fin = open(input_file_src + 'next_top_num_list.csv', 'r')
    line_cnt = 0
    got_cnt = 0
    for line in fin.readlines():
        if any(num == line_cnt + 1 for num in last_win):
            next_list.append([])
            line = line.split(' ')
            for i in range(TOP_N * 2):
                next_list[-1].append(line[i])
            got_cnt += 1
            if got_cnt == 6: break    
        line_cnt += 1
    fin.close()
    # Validate data length
    v_l = TOP_N * 2
    if len(month_list) != v_l or len(date_list) != v_l or len(wd_list) != v_l or len(last_win) != 6: 
        os.error('Length error, stop')
    # convert str to int in each list
    month_list = [int(num) for num in month_list]
    date_list = [int(num) for num in date_list]
    wd_list = [int(num) for num in wd_list]
    '''
    print(month_list)
    print(date_list)
    print(wd_list)
    print(next_list)
    '''
    
    # begin calculator
    number_list = []
    for i in range(69):
        number_list.append(0)
    # 1 - month list
    m_l_sum = sum(num for num in month_list[10:])
    m_l_cnt = 0
    for num in month_list[:10]:
        p = FACTOR * month_list[m_l_cnt + TOP_N] / m_l_sum 
        m_l_cnt += 1
        number_list[num - 1] += p
    # 2 - date list
    d_l_sum = sum(num for num in date_list[10:])
    d_l_cnt = 0
    for num in date_list[:10]:
        p = FACTOR * date_list[d_l_cnt + TOP_N] / d_l_sum
        d_l_cnt += 1
        number_list[num - 1] += p
    # 3 - weekday list
    wd_l_sum = sum(num for num in wd_list[10:])
    wd_l_cnt = 0
    for num in wd_list[:10]:
        p = FACTOR * wd_list[wd_l_cnt + TOP_N] / wd_l_sum
        wd_l_cnt += 1
        number_list[num - 1] += p
    # 4 - next list
    for each_num in next_list:
        n_l_sum = sum(int(num) for num in each_num[10:])
        n_l_cnt = 0
        for num in each_num[:10]:
            p = (FACTOR / 6) * int(each_num[n_l_cnt + TOP_N]) / n_l_sum
            n_l_cnt += 1
            number_list[int(num) - 1] += p

    # conlcusion
    num_list_argmax = sorted(range(len(number_list)), key=lambda k:number_list[k])[::-1]
    number_list = sorted(number_list)[::-1]
    if not os.path.exists(final_file_path):
        os.mkdir(final_file_path)
    fout = open(final_file_path + '_'+ str(year) + str(month) + str(day) + '.csv', 'w')
    for i in range(20):
        msg = 'Top {} number {} prob is {:.2f}%'.format(i + 1, num_list_argmax[i], number_list[i] * 100)
        print(msg)
        fout.write(msg + '\n')
    print('[Done, also a copy is saved at ./data/conclusion]')


def main():
    if os.path.exists(OUT_PATH):
        if len([name for name in os.listdir(OUT_PATH)]) == GENERATED_FILE_NUM:
            get_most_possible_num()
    else:
        print('[Detected: No required files, now generating files]')
        get_each_top()
        print('[Done, please run this file again]')


if __name__ == '__main__':
    main()

