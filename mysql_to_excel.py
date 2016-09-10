"""
Querying MySQL and writing to a XLS file.

Objective: We will connect to a MySQL database and query rows, which then we will output to a excel file.

Description: Actually Python is an usefull language that many Software/DevOp/Data Engineers turn to when performing a functional task. 
Although Python supports multiple programming paradigms (object-oriented, imperative and functional programming or procedural styles), 
we will be writing a small program that allows us to use Python as a functional language.

Requirements:
- Python 2.7.x ou superior
- Libraries: MySQLdb, xlwt

How it works:

1) To install a MySQL connector, type in the following command in the terminal window. 
If you do not have pip installed then please install pip by typing "sudo easy_isntall pip" into the terminal window:

	$ pip install MySQL-python
	$ pip install xlwt

2) Create a new Python file and type in the following.
"""

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
import xlwt


#Instantiates a workbook and sheet to write the query results to
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("Sheet1") # name of the worksheet


#Database connection
db = MySQLdb.connect(host="localhost", # your host, usually localhost
					user="arif", # your username
					passwd="arifisawesome", # your password
					db="arifsdb") # name of the data base


# you must create a Cursor object. It will let
# you execute all the queries you need
cur = db.cursor()


# Use all the SQL you like
cur.execute("SELECT * FROM YOUR_TABLE_NAME")

rowNum = 0 #keep track of rows
colNum = 0 #keep track of columns


# print all the cells of the row to excel sheet
for row in cur.fetchall() :
	sheet.write(rowNum, colNum, row) # row, column, value
	rowNum = rowNum + 1
	colNum = colNum + 1