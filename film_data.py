# -*- coding: utf-8 -*-
"""
@Time ： 2022/3/26 14:44
@Auth ： 吉吉
@File ：1.py
@IDE ：PyCharm
@Description : 未添加描述
"""

# 根据附件中在线电影影评的大数据信息，对数据进行相关处理。
# 要求：
# 1：在影评数据中提取影片ID信息（数据去重）
# 2：对影评数据进行分组与排序 ，将影评数据信息按照影评分数降序的顺序进行排序。
# 3：将影评数据按照用户编号 ，将每个用户影评分数前三的影评数据进行提取。
# 4：统计每部电影的总评分与平均评分
# 5：统计每部电影评分最高的前5条记录


import numpy as np
import pandas as pd

filepath = "C:/Users/22874/Desktop/新建文件夹/"
filename = filepath+'电影评分数据.txt'
df = pd.read_csv(filename, sep=',') # 读取数据

# 提取影片ID并去重
filemId = df['filmId'].drop_duplicates().sort_values(ascending=True)
filemId.to_csv(filepath+'影片ID.csv',index=False)

#将影评数据信息按照影评分数降序的顺序进行排序
df1 = df.sort_values(['filmId','pref'], ascending=[1,0])
grouped1 = df1.groupby(['filmId']).apply(lambda x:x[:])
# print(grouped1)
grouped1.to_csv(filepath+'影评分数降序.csv',index=False)

#每个用户影评分数前三的影评数据进行提取
df2 = df.sort_values(['userId','pref'],ascending=[1,0])     # 设置userId升序，pre降序
grouped2 = df2.groupby(['userId']).head(3)         # 设置显示每个useId前三个内容
grouped2.to_csv(filepath+'每个用户影评分数前三.csv',index=False)

# 4：统计每部电影的总评分与平均评分
df3 = df.groupby('filmId')['pref'].agg(['mean',np.sum])
df3.to_csv(filepath+'每部电影的总评分与平均评分.csv')


# 5：统计每部电影评分最高的前5条记录
df4 = df.sort_values(['filmId','pref'],ascending=[1,0])
grouped4 = df4.groupby(['filmId']).head(5)
grouped4.to_csv(filepath+'每部电影评分最高的前5.csv',index=False)

print('运行完成')
