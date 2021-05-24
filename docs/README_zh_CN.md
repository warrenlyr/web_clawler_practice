# web_clawler_first
* 第一个网络爬虫项目
* Warren Liu
* 2021/5/17

## 关于 ##
* 想做一个关于彩票（美国Powerball）预测的AI， 需要从官网爬虫数据下来。但是之前没有网络爬虫的相关经验，所以我决定做一个网络爬虫的项目。这是我第一次写网络爬虫。
* 2021/5/23：在此期间我做了很多搜索和尝试，我发现做一个关于彩票预测的AI是不现实的因为这个彩票数字的出现是根本没有规律的，网上一些关于彩票预测AI的项目最后的预测准确率均低于0.01%（或者说根本没有成功过），这种AI的准确预测率甚至低于直接走进7-11去买一张彩票的中奖率。所以我决定不做AI了，直接用爬虫下来的数据做一个概率分析。

## 更新 ##
* Version 0.2 - 5/22
    - 添加任务可视化进度条
    - 现在支持2001年以下的数据爬虫了
       2001年以上的数据每条数据有7个数字（5个彩票数字，一个powerball数字，和一个翻倍率数字），2001年以下的数据每条数据只有6个数字（5个彩票数字和一个powerball数字）
    - 删除了不必要的2021年-2002年数据中的翻倍率数字
    - 删除了爬2001年数据因为2001年数据有些月份有7个数字有些月份有6个数字
    - 现在可以用file_merge.py把爬下来的数据整合进一个文件了
* Version 0.3 - 5/23
    - ~~放弃用爬虫的数据做AI了~~:skull:
    - 添加data_analyze.py，用于计算下次开奖前20个最大可能出现的数字
    - 结束此项目

## 运行 ##
- py/py3/python3 根据不同系统使用不同前缀
```
py web_crawler.py
py file_merge.py
py data_analyze.py
```

## 数据储存方式 ##
* 所有数据都储存在 ./data/ 文件夹里
* 网络爬虫下来的数据储存在 ./data/all_years/ 文件夹里，以年份命名
* 整合的文件储存在 ./data/merged_file/ 文件夹里
* 所有由data_analyzed.py产生的数据储存在 ./data/analyzed_data/ 文件夹里
* 一份前20最大可能出现数字的副本储存在 ./data/conclusion/ 文件夹里

## 需求 ##
* Python 3
### 包 ###
|   包 |   链接    |
|-----------|-----------|
|requests | https://pypi.org/project/requests/|
|bs4 | https://pypi.org/project/beautifulsoup4/|
|dateutil | https://pypi.org/project/python-dateutil/|
|tqdm | https://pypi.org/project/tqdm/|