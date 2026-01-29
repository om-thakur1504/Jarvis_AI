import csv
import sqlite3 as sql
conn = sql.connect("dynamo.db")
cursor = conn.cursor()
# query = "CREATE TABLE IF NOT EXISTS sys_commands(Id INTEGER PRIMARY KEY, Name VARCHAR(100), Path VARCHAR(1000))"
# cursor.execute(query)
# # query = "INSERT INTO sys_commands VALUES(null, 'one note', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE')"
# # cursor.execute(query)
# # conn.commit()
# query = "CREATE TABLE IF NOT EXISTS web_commands(Id INTEGER PRIMARY KEY, Domain VARCHAR(100), URL VARCHAR(1000))"
# cursor.execute(query)
# # query = "INSERT INTO web_commands VALUES(null, 'youtube', 'https://www.youtube.com/')"
# # cursor.execute(query)
# # conn.commit()
# query = "INSERT INTO web_commands VALUES(null, 'google', 'https://www.google.com/')"
# cursor.execute(query)
# conn.commit()
# cursor.execute('''DROP TABLE IF EXISTS Contacts''')
# cursor.execute('''CREATE TABLE IF NOT EXISTS Contacts(Id INTEGER PRIMARY KEY, Name VARCHAR(200), Mobile No VARCHAR(255), email VARCHAR(255) NULL)''')
# desired_columns_indices = [0, 20]
# with open('contacts.csv', 'r', encoding = 'utf-8') as csvfile :
#     csvreader = csv.reader(csvfile)
#     for row in csvreader :
#         selected_data = [row[i] for i in desired_columns_indices if i < len(row)]
#         cursor.execute('''INSERT INTO Contacts(Id, 'Name', 'Mobile') VALUES(null, ?, ?)''', tuple(selected_data))
# conn.commit()
# conn.close()
# query = "Mumma"
# query = query.strip().lower()
# cursor.execute("SELECT Mobile FROM Contacts WHERE LOWER(Name) LIKE ? OR LOWER(Name) LIKE ?", ("%" + query + "%", query + "%"))
# results = cursor.fetchall()
# print(results[0][0])