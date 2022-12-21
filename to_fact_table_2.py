# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 18:27:00 2022

@author: UNPAR
"""

import pandas as pd

time_table = pd.read_csv('time_table2.csv', names=['day', 'date', 'month', 'year'])
product_table = pd.read_csv('product_table2.csv', names=['product_name', 
                                               'category'])

review_table = pd.read_csv('all_item.csv', names= ['index', 'day', 'date_review', 'month_review', 
       'year_review', 'product_name', 'category', 
       'review_comment', 'rating', 'vote_score', 'product_category'])


for i in range(1, len(review_table.value_counts()) + 1):
    review_table['index'][i] = i;
    
arr_index = []   
for i in range(1, len(review_table.value_counts()) + 1):
    arr_index.append(i)
    
review_table['product_key'] = arr_index
review_table['time_key'] = arr_index

arr_index = []   
for i in range(1, len(product_table.value_counts()) + 1):
    arr_index.append(i)
    
product_table['product_key'] = arr_index

arr_index = []   
for i in range(1, len(time_table.value_counts())+1):
    arr_index.append(i)
    
time_table['time_key'] = arr_index


for i in range(len(product_table.values)):
    #print(i)
    for j in range(len(review_table.values)):
       #print(j)
       if (review_table.values[j][5] == product_table.values[i][0]):
           print(review_table.values[j][3] == product_table.values[i][0])
           print(product_table.values[i][0])
           print("append " + str(product_table.values[i][2]))
           review_table['product_key'][j] = (product_table.values[i][2])


for i in range(len(time_table.values)):
    #print(i)
    for j in range(len(review_table.values)):
       #print(j)   
       if (review_table.values[j][2] == time_table.values[i][1] 
            and review_table.values[j][3]== time_table.values[i][2] 
            and review_table.values[j][4]== time_table.values[i][3]):
           print(review_table.values[j][2] == time_table.values[i][1] 
                and review_table.values[j][3]== time_table.values[i][2] 
                and review_table.values[j][4]== time_table.values[i][3])
           review_table['time_key'][j] = (time_table.values[i][4])    
           

product_table = product_table[["product_key", "product_name", "category"]]
time_table = time_table[["time_key", "day", "date", "month", "year"]]

review_table = review_table[["index","product_key","time_key", "review_comment", "vote_score", "rating"]]
review_table.rename(columns={"index" : "id_review"}, inplace=True)

from hdfs import InsecureClient #import library hdfs
client_hdfs = InsecureClient('http://localhost:9870') #connect ke hdfs

hdfs_path = '/user/hive/data_tubes/result'

with client_hdfs.write(hdfs_path+'/'+'review.csv', encoding='utf-8') as writer:
    review_table.to_csv(writer, index=False)

with client_hdfs.write(hdfs_path+'/'+'product.csv', encoding='utf-8') as writer:    
    product_table.to_csv(writer, index=False)
    
with client_hdfs.write(hdfs_path+'/'+'time.csv', encoding='utf-8') as writer:
    time_table.to_csv(writer, index=False)

review_table.to_csv('fact_dimension_table/review.csv', index=False)

    