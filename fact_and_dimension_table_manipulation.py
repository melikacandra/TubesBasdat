# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 00:14:50 2022

@author: UNPAR
"""

index = 0
for value in new_beauty['product_name']:
    nama_product = value
    sudah_diganti = nama_product.replace(',', '')
    #print(sudah_diganti + ' vs ' + nama_product)
    new_beauty['product_name'][index] = sudah_diganti
    index = index + 1
    
import pandas as pd

df_date = pd.read_csv('date.csv', names=['day', 'month', 'year'])
df_product = pd.read_csv('product.csv', names=['product_name', 
                                               'category'])
df_review = pd.read_csv('review_item.csv', 
                        names=['index', 'day_review', 'month_review', 
                               'year_review', 'product_name', 'category', 
                               'review_comment', 'rating', 'vote_score', 'product_category'])

df_review.reset_index()
df_review.drop('index',inplace=True, axis=1)

arr_key_date_for_review = []
for i in range(len(df_date.values)):
    #print(i)
    for j in range(len(df_review.values)):
       #print(j)
       
       if (df_review.values[j][0] == df_date.values[i][0] 
            and df_review.values[j][1]== df_date.values[i][1] 
            and df_review.values[j][2]== df_date.values[i][2]):
           print(df_review.values[j][0] == df_date.values[i][0] 
                 and df_review.values[j][1]== df_date.values[i][1] 
                 and df_review.values[j][2]== df_date.values[i][2])
           print(df_date.values[i][3])
           print("append " + str(df_date.values[i][3]))
           print("date " + str(df_date.values[i]))
           print("review " + str(df_review.values[j]))
           df_review['date_key'][j] = (df_date.values[i][3])
           
arr_key_product_for_review = []
for i in range(len(df_product.values)):
    #print(i)
    for j in range(len(df_review.values)):
       #print(j)
       if (df_review.values[j][3] == df_product.values[i][0]):
           print(df_review.values[j][3] == df_product.values[i][0])
           print(df_product.values[i][0])
           print("append " + str(df_product.values[i][2]))
           df_review['product_key'][j] = (df_product.values[i][2])
            
            
df_review['date_key'] = arr_key_date_for_review
    
df_date.values[0] 
df_review.values[0]
df_review.values[0][0] == df_date.values[0][0]
df_review.values[0][1] == df_date.values[0][1]
df_review.values[0][2] == df_date.values[0][2]

    
    
n_date = len(df_date)
n_product = len(df_product)


arr_key_date = []
for value in range(1, n_date+1):
    arr_key_date.append(value)
    
arr_key_product = []
for value in range(1, n_product+1):
    arr_key_product.append(value)
    
df_date['date_key'] = arr_key_date
df_product['product_key'] = arr_review
arr_review = []

for value in range(len(df_review.values)):
    arr_review.append(value)
    
    
df_review['product_key'] = arr_review


new_df_review = df_review.drop(['day_review', 'month_review', 'year_review', 'category', 'product_category' ], axis = 1)
new_df_review = new_df_review[['product_key', 'time_key', 'review_comment', 'vote_score', 'rating']]


df_date.rename(columns={"date_key" : "time_key"}, inplace=True)

df_review.rename(columns={"date_key" : "time_key"}, inplace=True)

new_df_review.rename(columns={"date_key" : "time_key"}, inplace=True)

import pandas as pd #import library pandas
from hdfs import InsecureClient #import library hdfs
client_hdfs = InsecureClient('http://localhost:9870') #connect ke hdfs




