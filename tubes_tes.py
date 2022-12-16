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

#DATA CLEANING
#jadi lower case semua 
df['review'] = df['review'].str.lower()
    
#bersihin unicode
for i in range(0,100):
    text = df.review[i]
    text = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", text)
    df.review[i] = text
    
#bersihin stop words
stop = stopwords.words('english')
for i in range(0,100):
    text = df.review[i]
    text = " ".join([word for word in text.split() if word not in (stop)])
    df.review[i] = text

df.to_csv('C:/UNPAR/sem_7/Big_data/Tugas_Besar/data_drug.csv')
    
