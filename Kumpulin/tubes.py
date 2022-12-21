# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 17:02:45 2022

@author: Lenovo
"""

import pandas as pd
import nltk.corpus
nltk.download('stopwords')
from nltk.corpus import stopwords
import re

df = pd.read_csv("DATASET TA/amazon_beauty_reviews.csv")

df.dtypes
#product_title, review_headlines + review_body (gabung jadi 1)
#product_id dipakai -> diedit dari 1, 2, 3, ...

"""
Data Cleaning

"""
#clean data convert object jadi string
df['marketplace'] = df['marketplace'].astype('string')
df['review_id'] = df['review_id'].astype('string')
df['product_id'] = df['product_id'].astype('string')
df['product_title'] = df['product_title'].astype('string')
df['product_category'] = df['product_category'].astype('string')
df['review_headline'] = df['review_headline'].astype('string')
df['review_body'] = df['review_body'].astype('string')
df['review_date'] = df['review_date'].astype('string')

df.dtypes

#hapus kolom lain yang ga dipake
df_new = df[['review_date','product_title','star_rating','review_headline', 'review_body', 'helpful_votes', 'product_category']]

#pisahkan tanggal 31/08/2015
date = df_new['review_date']
for i in range(0,100):   
    ambil_tanggal = date[i]
    list_date = ambil_tanggal.split('/')
    df_new['date'] = list_date[0]
    df_new['month'] = list_date[1]
    df_new['year'] = list_date[2]

df_new.dtypes

#ubah date, month, year menjadi int
df_new['date'] = df_new['date'].astype(int)
df_new['month'] = df_new['month'].astype(int)
df_new['year'] = df_new['year'].astype(int)


# Using Series.str.cat() function 
#df_new['review'] = df_new['review_headline'] + ' ' + df_new['review_body']
df_new["review"] = df_new["review_headline"].str.cat(df_new["review_body"], sep = " ")

#star rating x 2 agar range 1-10
df_new['star_rating'] = df_new['star_rating']*2

#jadi lower case semua 
df_new['review'] = df_new['review'].str.lower()
    
#bersihin unicode
for i in range(0,100):
    text = df_new.review[i]
    text = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", text)
    df_new.review[i] = text
    
#bersihin stop words
stop = stopwords.words('english')
for i in range(0,100):
    text = df_new.review[i]
    text = " ".join([word for word in text.split() if word not in (stop)])
    df_new.review[i] = text

#rename column name
df_new = df_new.rename(columns = {'product_title':'product_name','star_rating':'rating', 'product_category':'category', 'helpful_votes':'vote_score'})

#kolom diurutkan sesuai yang diinginkan
df_new = df_new[['date','month', 'year','product_name', 'category', 'review', 'rating', 'vote_score']]

#df_new.to_csv('C:/UNPAR/sem_7/Big_data/Tugas_Besar/new_beauty.csv')

