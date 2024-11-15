# START
# The keyword global indicates that a certain variable is global, meaning it exists outside of the function.
# Using global allows a function to modify the value of a global variable.

# Disadvantages:
# Makes code harder to understand and manage.
# Increases the likelihood of bugs.
# Limits the use of parallel processing and creates strong dependencies between different parts of the code.


#x: int = 1
#def foo():
#    print(x)  # Attempting to access the variable before it is defined locally
#    x = 4  # x is treated as a local variable in the function
#foo()

# Explanation:
# Due to the assignment x = 4, the function treats x as a local variable instead of referring to the global x.
# At the line print(x), the local variable has not yet been defined and cannot use globle and then change the value without using the globle keyword, leading to an error.
# END
