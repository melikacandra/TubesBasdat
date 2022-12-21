# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pymysql

connection = pymysql.connect(host="localhost", 
                             port=3307, 
                             user="root", 
                             passwd="melikacantik", database="tubes_basdat")
cursor = connection.cursor()

cursor.execute("select * from review_table")
review_table = cursor.fetchall()
cursor.execute("select * from product_table")
product_table = cursor.fetchall()
cursor.execute("select * from time_table")
time_table = cursor.fetchall()


import datetime
dt = '21/12/2022'
day, month, year = (int(x) for x in dt.split('/'))    
ans = datetime.date(year, month, day)
print (ans.strftime("%A"))