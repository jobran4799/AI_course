# START
grade: int = int(input("what is your grade?"))
if grade >= 0 and grade < 41:
    print("try harder next time...")
elif grade > 40 and grade < 61:
    print("you're getting there, need some more work")
elif grade > 60 and grade < 81:
    print("good pretty")
elif grade > 80 and grade < 96:
    print("!awesome")
elif grade > 95 and grade < 101:
    print("excellent!!!")
else:
    print("grade illegal")
# END
