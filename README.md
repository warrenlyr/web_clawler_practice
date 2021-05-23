# web_clawler_first
* Warren Liu
* May 17 2021

## About ##
* Wanted to train an AI about Lotto based on winning numbers history, but I do not have experience with web clawler. Thus, I decided to get all winning numbers from Lotto myself. This is my first project about web clawler.
*  Version 0.2 Updates:
   1. Added track for the task
   2. Now support year under 2001 
       year above 2001 have 7 numbers [5 numbers + 1 powerball + 1 power play number], year under 2001 have 6 numbers [5 numbers + 1 powerball]
   3. Deleted the powerplay number from year 2021 - 2002 because it is unnecessary
   4. Removed year 2001 because it contains both 7 numbers and 6 numbers in different month
   5. Now can use file_merge.py to merge mutiple data files into one file

## To run ##
```
py main.py
```