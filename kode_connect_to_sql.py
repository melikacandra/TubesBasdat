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
cursor.execute("select * from product_table")
output = cursor.fetchall()