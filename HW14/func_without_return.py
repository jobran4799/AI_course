# START

def my_ascending(num1: int = 0, num2: int = 0):
    if num1 < num2:
        for i in range(num1, num2, 1):
            print(i, end=" ")
    else:
        for i in range(num2, num1, 1):
            print(i, end=" ")
    print()





def my_details(string: str = ''):
    if string:
        print(f"{string[0]},{string[len(string) // 2]},{string[-1]}")





def say_bool(boolean: bool):
    if boolean:
        print("True")
    else:
        print("False")





def zugi_print(lis: list[int]):
    if lis:
        for item in lis:
            if item % 2 == 0:
                print(f"{item} is even")
            else:
                print(f"{item} is odd")





def my_statistics(lis: list[float]):
    average: float = 0
    if lis:
        for item in lis:
            average += item
        print("max number ", max(lis))
        print("min number ", min(lis))
        print("count number ", len(lis))
        print("average ", average / len(lis))




# END
