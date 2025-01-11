import sqlite3


conn = sqlite3.connect("hw_solution.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS shopping (
    id INTEGER PRIMARY KEY,
    name TEXT,
    amount INTEGER
)
""")


cursor.execute("INSERT INTO shopping VALUES (1, 'Avokado', 5)")
cursor.execute("INSERT INTO shopping VALUES (2, 'Milk', 2)")
cursor.execute("INSERT INTO shopping VALUES (3, 'Bread', 3)")
cursor.execute("INSERT INTO shopping VALUES (4, 'Chocolate', 8)")
cursor.execute("INSERT INTO shopping VALUES (5, 'Bamba', 5)")
cursor.execute("INSERT INTO shopping VALUES (6, 'Orange', 10)")


cursor.execute("SELECT * FROM shopping")

for row in cursor.fetchall():
    print(row)


cursor.execute("SELECT * FROM shopping WHERE amount > 5")
print("\nItems with amount > 5:")
for row in cursor.fetchall():
    print(row)


cursor.execute("DELETE FROM shopping WHERE name LIKE 'Orange'")


cursor.execute("UPDATE shopping SET name = 'Bisli' WHERE name LIKE 'Bamba'")


cursor.execute("UPDATE shopping SET amount = 1 WHERE name LIKE 'Milk'")


cursor.execute("SELECT COUNT(*) FROM shopping")
print("\nNumber of items:", cursor.fetchone()[0])


cursor.execute("SELECT * FROM shopping WHERE id > 0")
print("\nFinal items:")
for row in cursor.fetchall():
    print(row)

conn.commit()
conn.close()
