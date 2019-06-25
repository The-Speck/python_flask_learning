import sqlite3

connection = sqlite3.connect('python-flask.db')

cursor = connection.cursor()

drop_table = "DROP TABLE IF EXISTS users"
cursor.execute(drop_table)

create_table = "CREATE TABLE users (id integer PRIMARY KEY AUTOINCREMENT, username text, password text)"
cursor.execute(create_table)

user = ('Alex', 123)
insert_user = "INSERT INTO users ('username', 'password') VALUES (?, ?)"
cursor.execute(insert_user, user)

users = [
  ('Bob', 456),
  ('Alice', 789)
]
cursor.executemany(insert_user, users)

select_all_users = "SELECT * FROM users" 
for row in cursor.execute(select_all_users):
  print(row)

connection.commit()
connection.close()
