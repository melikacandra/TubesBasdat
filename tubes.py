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

df = pd.read_csv("DATASET_TA/amazon_beauty_reviews.csv")

#product_title, review_headlines + review_body (gabung jadi 1)
#product_id dipakai -> diedit dari 1, 2, 3, ...

#DATA CLEANING
#hapus kolom lain yang ga dipake
df_new = df[['product_id','product_title', 'review_headline', 'review_body']]

df_new.describe()

# Using Series.str.cat() function 
#df_new['review'] = df_new['review_headline'] + ' ' + df_new['review_body']
df_new["review"] = df_new["review_headline"].str.cat(df_new["review_body"], sep = " ")

df_new = df_new[['product_id', 'product_title', 'review']]

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

    




    