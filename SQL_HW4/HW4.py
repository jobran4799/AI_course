import sqlitelib


# Create tables
def create_tables(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        course_id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic TEXT,
        hours INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS grades (
        student_id INTEGER,
        course_id INTEGER,
        grade REAL,
        PRIMARY KEY (student_id, course_id),
        FOREIGN KEY (student_id) REFERENCES students(student_id),
        FOREIGN KEY (course_id) REFERENCES courses(course_id)
    )
    """)


# Add sample data
def insert_sample_data(cursor):
    # Add courses
    cursor.execute("INSERT INTO courses (topic, hours) VALUES (?, ?)", ("Mathematics", 40))
    cursor.execute("INSERT INTO courses (topic, hours) VALUES (?, ?)", ("Physics", 30))

    # Add students
    cursor.execute("INSERT INTO students (name, email) VALUES (?, ?)", ("Alice", "alice@example.com"))
    cursor.execute("INSERT INTO students (name, email) VALUES (?, ?)", ("Bob", "bob@example.com"))

    # Add grades
    cursor.execute("INSERT INTO grades (student_id, course_id, grade) VALUES (?, ?, ?)", (1, 1, 85))
    cursor.execute("INSERT INTO grades (student_id, course_id, grade) VALUES (?, ?, ?)", (1, 2, 90))
    cursor.execute("INSERT INTO grades (student_id, course_id, grade) VALUES (?, ?, ?)", (2, 1, 78))
    cursor.execute("INSERT INTO grades (student_id, course_id, grade) VALUES (?, ?, ?)", (2, 2, 88))


# Query to calculate average grades
def calculate_course_averages(cursor):
    cursor.execute("SELECT course_id, AVG(grade) as avg_grade FROM grades GROUP BY course_id")
    return cursor.fetchall()


# Display all courses
def display_courses(cursor):
    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()
    for course in courses:
        print(dict(course))


# Add a new course with user input
def add_course(cursor, conn):
    topic = input("Enter course topic: ")
    hours = int(input("Enter course hours: "))

    # Check if course already exists
    cursor.execute("SELECT * FROM courses WHERE topic = ?", (topic,))
    if cursor.fetchone():
        print("Error: A course with this topic already exists.")
    else:
        cursor.execute("INSERT INTO courses (topic, hours) VALUES (?, ?)", (topic, hours))
        conn.commit()
        print("Course added successfully.")



