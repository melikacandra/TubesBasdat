# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 15:17:51 2022

@author: Lenovo
"""

import pandas as pd
import nltk.corpus
nltk.download('stopwords')
from nltk.corpus import stopwords
import re

df = pd.read_csv("DATASET_TA/drug_reviews.csv")

df.dtypes

#DATA CLEANING

#bersihkan yang semua tipe objek jadi string
df['condition'] = df['condition'].astype('string')
df['date'] = df['date'].astype('string')
df['drugName'] = df['drugName'].astype('string')

#cek apakah sudah terconvert
df.dtypes

df_new = df[['date','drugName','rating','review','usefulCount']]
df_new['category'] = 'Drug'

df_new['tanggal'] = ''
df_new['month'] = ''
df_new['year'] = ''

#datenya dipisah May 20, 2012
date = df_new['date']
for i in range(0,100):   
    ambil_tanggal = date[i]
    list_date = ambil_tanggal.split(' ')
    df_new.month[i] = list_date[0]
    df_new.tanggal[i] = list_date[1]
    df_new.year[i] = list_date[2]

#ubah nama bulan jadi angka
df_new['month'] = df_new['month'].replace('January', 1)
df_new['month'] = df_new['month'].replace('February', 2)
df_new['month'] = df_new['month'].replace('March', 3)
df_new['month'] = df_new['month'].replace('April', 4)
df_new['month'] = df_new['month'].replace('May', 5)
df_new['month'] = df_new['month'].replace('June', 6)
df_new['month'] = df_new['month'].replace('July', 7)
df_new['month'] = df_new['month'].replace('August', 8)
df_new['month'] = df_new['month'].replace('September', 9)
df_new['month'] = df_new['month'].replace('October', 10)
df_new['month'] = df_new['month'].replace('November', 11)
df_new['month'] = df_new['month'].replace('December', 12)

#hapus , dari tanggal
tgl = df_new['tanggal']
for i in range(0,100):   
    ambil_tanggal = tgl[i]
    list_date = ambil_tanggal.split(',')
    df_new.tanggal[i] = list_date[0]

df_new.dtypes

#convert tipe data lagi 
df_new['category'] = df_new['category'].astype('string')

#ubah date, month, year menjadi int
df_new['tanggal'] = df_new['tanggal'].astype(int)
df_new['month'] = df_new['month'].astype(int)
df_new['year'] = df_new['year'].astype(int)

df_new.dtypes

df_new = df_new[['tanggal','month','year','drugName','category','review','rating','usefulCount']]

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
    
df_new['review'] = df_new['review'].astype('string')
df_new['review'] = df_new['review'].replace('/"', '')

#rename column name
df_new = df_new.rename(columns = {'drugName':'product_name','usefulCount':'vote_score','tanggal':'date'})

#kolom diurutkan sesuai yang diinginkan
df_new = df_new[['date','month', 'year','product_name', 'category', 'review', 'rating', 'vote_score']]

df_new.dtypes

df_new.to_csv('C:/UNPAR/sem_7/Big_data/Tugas_Besar/new_drug.csv')