# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 17:24:27 2022

@author: UNPAR
"""

import pandas as pd
from hdfs import InsecureClient #import library hdfs

data_beauty = pd.read_csv('new_beauty2.csv')
data_apparel = pd.read_csv('new_apparel2.csv')
data_drug = pd.read_csv('new_drug2.csv')
data_jewelry = pd.read_csv('new_jewelry2.csv')
data_shoes = pd.read_csv('new_shoes2.csv')

client_hdfs = InsecureClient('http://localhost:9870') #connect
#tentukan path hdfs
hdfs_path = '/user/hive/data_tubes'
beauty_name = 'new_beauty.csv'
drug_name = 'new_drug.csv'
jewelry_name = 'new_jewelry.csv'
shoes_name = 'new_shoes.csv'
apparel_name = 'new_apparel.csv'


with client_hdfs.write(hdfs_path+'/'+beauty_name, encoding='utf-8') as writer:
    data_beauty.to_csv(writer, index=False)

with client_hdfs.write(hdfs_path+'/'+drug_name, encoding='utf-8') as writer:    
    data_drug.to_csv(writer, index=False)
    
with client_hdfs.write(hdfs_path+'/'+jewelry_name, encoding='utf-8') as writer:
    data_jewelry.to_csv(writer, index=False)

with client_hdfs.write(hdfs_path+'/'+shoes_name, encoding='utf-8') as writer:    
    data_shoes.to_csv(writer, index=False)

with client_hdfs.write(hdfs_path+'/'+apparel_name, encoding='utf-8') as writer:    
    data_apparel.to_csv(writer, index=False)
