# web_clawler_first
* Warren Liu
* May 17 2021

## About ##
* Wanted to train an AI about Lotto based on winning numbers history, but I do not have experience with web clawler. Thus, I decided to get all winning numbers from Lotto myself. This is my first project about web clawler.
* 2021/5/23: After many researches and tryings, I found out that making an AI on Lotto is impossible because it is irregular, the prediction accuracy of many projects of the same topic have accuracy under 0.01%, which is lower than the probability if you just buy a ticket at a 7-11. I am completing this project just based on the probability.

## Updates ##
* Version 0.2 - 5/22
    1. Added track for the task
    2. Now support year under 2001 
       year above 2001 have 7 numbers [5 numbers + 1 powerball + 1 power play number], year under 2001 have 6 numbers [5 numbers + 1 powerball]
    3. Deleted the powerplay number from year 2021 - 2002 because it is unnecessary
    4. Removed year 2001 because it contains both 7 numbers and 6 numbers in different month
    5. Now can use file_merge.py to merge mutiple data files into one file
* Version 0.3 - 5/23
    1. Give up trainning an AI based on this data
    2. Added data_analyze.py to calculate the top 20 winning numbers for the next game with probality
    3. Closed this project

## To run ##
```
py web_crawler.py
```
```
py file_merge.py
```
```
py data_analyze.py
```

## How data stores ##
* All data will store under 'data' folder
* Original Powerball winning numbers files will be stored at ./data/all_years/
* Merged files will be stored under ./data/merged_file/
* All files generated by data_analyze.py will be stored under ./data/analyzed_data/
* A copy of outcome will be stored under ./data/conclusion/

## Requirements ##
* Python 3
**Packages**
* requests
* bs4
* dateutil
* tqdm