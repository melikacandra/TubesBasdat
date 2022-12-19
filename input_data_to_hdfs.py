# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 14:47:11 2022

@author: UNPAR
"""

import pandas as pd #import library pandas
from hdfs import InsecureClient #import library hdfs
client_hdfs = InsecureClient('http://localhost:9870') #connect ke hdfs


#tentukan path hdfs
hdfs_path = '/user/hive/data_tubes'
beauty_name = 'new_beauty.csv'
drug_name = 'new_drug.csv'




#masukkan data
new_beauty = pd.read_csv(beauty_name)
new_drug = pd.read_csv(drug_name)
#tes masukin ke hdfs sebagai csv
with client_hdfs.write(hdfs_path+'/'+beauty_name, encoding='utf-8') as writer:
    new_beauty.to_csv(writer, index=False)

with client_hdfs.write(hdfs_path+'/'+drug_name, encoding='utf-8') as writer:    
    new_drug.to_csv(writer, index=False)