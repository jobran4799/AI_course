# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sqlitelib
import HW4

def exeute():
    db_name = "university.db"
    conn, cursor = sqlitelib.connect_db(db_name)

    # Create tables
    HW4.create_tables(cursor)

    # Insert sample data
    HW4.insert_sample_data(cursor)
    conn.commit()

    # Display courses
    print("All courses:")
    HW4.display_courses(cursor)

    # Calculate course averages
    print("\nCourse Averages:")
    averages = HW4.calculate_course_averages(cursor)
    for course_id, avg_grade in averages:
        print(f"Course ID {course_id}: Average Grade = {avg_grade}")

    # Add a new course
    print("\nAdd a new course:")
    HW4.add_course(cursor, conn)

    # Close the connection
    conn.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    exeute()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
