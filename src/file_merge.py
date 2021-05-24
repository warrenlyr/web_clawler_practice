# -*- coding:utf-8 -*-
# Author: Warren Liu
# Date: 5/21/2021
# Project: Merge multiple files into one file

import os
from tqdm import tqdm


OUT_PATH = r'./data/merged_file/'
FILE_PATH = r'./data/all_years/'
FILE_NAMES = os.listdir(FILE_PATH)
OUT_FILE = r'merged_file.csv'

# merge files into one file
def merge_file():
    if not os.path.exists(OUT_PATH):
        os.mkdir(OUT_PATH)
    out_file = open(OUT_PATH + OUT_FILE, 'w')

    for file in FILE_NAMES:
        this_file_path = FILE_PATH + file
        #print(r'Now writting file {} to {}'.format(file, OUT_FILE))
        for line in open(this_file_path):
            out_file.writelines(line)

    print('[Done merging file]')
    out_file.close()


# get rid of the date in the file
def delete_date():
    in_file = OUT_PATH + OUT_FILE
    out_file = OUT_PATH + 'merged_file_without_date.csv'
    with open(in_file, 'r') as fin, open(out_file, 'w') as fout:
        for line in fin:
            l = line[10:]
            fout.writelines(l)
    print('delete_date: Input file lines: {} Output file lines: {}'.format(len(open(in_file).readlines()),(len(open(out_file).readlines()))))
    fin.close()
    fout.close()
    print('[Done deleting date]')


# get rid of the year in the file
def delete_year():
    in_file = OUT_PATH + OUT_FILE
    out_file = OUT_PATH + 'merged_file_without_year.csv'
    with open(in_file, 'r') as fin, open(out_file, 'w') as fout:
        for line in fin:
            l = line[5:]
            fout.writelines(l)
    print('delete_year: Input file lines: {} Output file lines: {}'.format(len(open(in_file).readlines()),(len(open(out_file).readlines()))))
    fin.close()
    fout.close()
    print('[Done deleting year]')



def main():
    merge_file()
    delete_date()
    delete_year()

if __name__ == '__main__':
    main()