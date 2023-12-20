import sqlite3

db_name = 'for_training.db'

connection = sqlite3.connect(db_name)
connection.close()

print(f"SQLite database '{db_name}' created successfully")

