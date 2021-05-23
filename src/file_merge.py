# -*- coding:utf-8 -*-
# Author: Warren Liu
# Date: 5/21/2021
# Project: Merge multiple files into one file

import os
from tqdm import tqdm


FILE_PATH = r'./data/'
FILE_NAMES = os.listdir(FILE_PATH)
OUT_FILE = r'merged_file.csv'

# merge files into one file
def merge_file():
    out_file = open(FILE_PATH + OUT_FILE, 'w')

    for file in FILE_NAMES:
        this_file_path = FILE_PATH + file
        print(r'Now writting file {} to {}'.format(file, OUT_FILE))
        for line in open(this_file_path):
            out_file.writelines(line)

    print('Done')
    out_file.close()


# get rid of the date in the file
def delete_date():
    in_file = FILE_PATH + OUT_FILE
    out_file = FILE_PATH + 'merged_file_without_date.cvs'
    with open(in_file, 'r') as fin, open(out_file, 'w') as fout:
        for line in fin:
            l = line[10:]
            fout.writelines(l)
    print('Input file lines: {} Output file lines: {}'.format(len(open(in_file).readlines()),(len(open(out_file).readlines()))))
    fin.close()
    fout.close()


# get rid of the year in the file
def delete_year():
    in_file = FILE_PATH + OUT_FILE
    out_file = FILE_PATH + 'merged_file_without_year.cvs'
    with open(in_file, 'r') as fin, open(out_file, 'w') as fout:
        for line in fin:
            l = line[5:]
            fout.writelines(l)
    print('Input file lines: {} Output file lines: {}'.format(len(open(in_file).readlines()),(len(open(out_file).readlines()))))
    fin.close()
    fout.close()


if __name__ == '__main__':
    #merge_file()
    #delete_date()
    delete_year()