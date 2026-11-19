import sqlite3
import time

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS test_tb (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    age INTEGER NOT NULL,
    grade TEXT NOT NULL
)
""")

conn.commit()


def add_user(name, age, grade):
    try:
        cursor.execute(
            'INSERT INTO test_tb (name, age, grade) VALUES (?, ?, ?)',
            (name, age, grade)
        )

        conn.commit()
        print("User added successfully")

    except sqlite3.IntegrityError as e:
        print(f"Type of error: {e}")
        time.sleep(3)
        print("User already exists")


def show_user():
    cursor.execute('SELECT * FROM test_tb')

    users = cursor.fetchall()

    if users:
        for user in users:
            print(f'ID: {user[0]}')
            print(f'NAME: {user[1]}')
            print(f'AGE: {user[2]}')
            print(f'GRADE: {user[3]}')
            print("-" * 30)
    else:
        print("No users found!")


add_user("vishal", 20, "A")
add_user("ritik", 21, "B")
add_user("shankar", 20, "A")

print('\nALL USERS:')
show_user()

conn.close()
