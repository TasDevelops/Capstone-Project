import sqlite3  # import sqlite
conn = sqlite3.connect('postcode_data')  # connecting our dataset to python
#print("Opened database successfully")  # print this when database is opened successfully

cur = conn.cursor()  # creating table for database
""" cur.execute(''' CREATE TABLE POSTCODE_DATABASE
 (  ID INT PRIMARY KEY           NOT NULL,
     Search_postcode      TEXT        NOT NULL,
     Date_Time       DATETIME         NOT NULL);''')

print("Table created successfully") """




postcode_data = (
    "INSERT INTO `POSTCODE_DATABASE` (`ID`, `Search_postcode`, `Data_Time`) "
    "VALUES (NULL, %s, '0')")
content = "... html ..."
cur.execute(postcode_data, [Search_postcode])
# connection_object.commit()
conn.commit()
conn.close() 

 
