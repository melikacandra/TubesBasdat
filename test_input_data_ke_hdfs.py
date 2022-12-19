# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 13:08:40 2022

@author: UNPAR
"""

import pandas as pd #import library pandas
from hdfs import InsecureClient #import library hdfs
client_hdfs = InsecureClient('http://localhost:9870') #connect ke hdfs

#baca data dan masukan sebagai dataframe
data_beauty_review = pd.read_csv('data_beauty.csv')


#tentukan path hdfs
hdfs_path = '/user/hive/input_from_python/beauty.csv'

#tes masukin ke hdfs sebagai csv
with client_hdfs.write(hdfs_path, encoding='utf-8') as writer:
    data_beauty_review.to_csv(writer, index=False)
    


