# START
# part a
# try-except is used in Python for error handling.
# The code inside the try block is executed, and if an error occurs,
# Python will jump to the except block to handle the error.
# This prevents the program from crashing due to unexpected errors
# and allows the code to continue running or handle the issue gracefully.

# part p
# Catching errors in Python is important to prevent the program
# from crashing unexpectedly.
# Instead of terminating the execution due to an error,
# you can handle it by displaying a friendly error message,
# retrying the operation, or taking other corrective actions.
# This makes the program more robust and user-friendly.

try:
    result = 88 / 0
except ZeroDivisionError as e:
    print(f"Error: {e} - Cannot divide by zero.")

try:
    raise ValueError("This is a custom error.")
except ValueError as e:
    print(f"Error: {e}")


numbers_list = [10, 20, 30, 40]

while True:
    try:
        user_input = input("Enter an index (or -999 to stop): ")

        if user_input == "-999":
            break

        index = int(user_input)

        print(f"The number at index {index} is: {numbers_list[index]}")

    except ValueError:
        print("Error: You must enter a valid number.")

    except IndexError:
        print(f"Error: Index {index} is out of range. Please enter a valid index.")

# END
