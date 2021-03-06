#!/usr/bin/env python3

import numpy as np
import pandas as pd
import sqlite3

# HERE USE SQL SYNTAX TO CREATE THE TABLE THAT WILL HOLD THE DATA SET YOUR TEAM WILL USE
query = """
INSERT SQL SYNTAX HERE TO CREATE THE TABLE 
RECALL THERE ARE 5 COLUMNS EACH MUST BE EXPLICITY CREATED WITH THE CORRECT DATA TYPE AND VARIABLE NAME
""";

# HERE WE'RE CONNECTING TO THE IN-MEMORY DATABASE
# THIS IS USEFUL BECAUSE YOU DON'T HAVE TO DOWNLOAD A DATABASE/CONNECT TO ONE USING CREDENTIALS
con = sqlite3.connect(':memory:')

con.execute(query) # HERE WE TELL THE CONNECTION TO EXECUTE THE QUERY CREATED THE TABLE
con.commit() # SAVE (COMMIT) THE CHANGES

# LET'S LOAD OUR DATA INTO A LIST THAT WILL BE EXECUTED LATER 
# HINT: JUST COPY PASTE THE CONTENTS OF THE FILE 'dataSource.txt' INTO THE LIST PROVIDED BELOW (AS IS)
data = []

# SQL QUERY THAT WILL INSERT OUR DATA INTO THE TABLE WE CREATED EARLIER
stmt = "SQL QUERY TO LOAD 'data' INTO TABLE YOU GENERATED EARLIER"

con.executemany(stmt, data)
con.commit()

# NOW USING SQL SYNTAX CHOOSE THE ENTIRE TABLE CONTENTS
cursor = con.execute('SQL QUERY TO GRAB ALL THE DATA IN THE TABLE GOES HERE')

# FOLLOWING COMMAND FETCHES ALL 
rows = cursor.fetchall()

# FINAL STEP IS LOADING THE QUERY CONTENTS INTO A PANDAS DATA FRAME
iris = pd.DataFrame(rows, columns = list(zip(*cursor.description))[0])

# PRINT FIRST 6 VALUES TO SEE IF YOU DID IT CORRECTLY
print(iris.head())

# FINAL STEP IS OUTPUT THE NEW FILE 