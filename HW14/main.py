# This is a sample Python script.
import func_with_return
import func_without_return


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    func_without_return.my_ascending(-12, 7)
    func_without_return.my_details("AI is the best")
    func_without_return.say_bool(True)
    func_without_return.say_bool(False)

    func_without_return.zugi_print([14, 14, 15, 10, 2, 3, 5, ])
    list1: list[float] = []
    while True:
        num: float = float(input("enter a number"))
        if num == -99:
            break
        list1.append(num)

    func_without_return.my_statistics(list1)

    avg1: float = func_with_return.my_avg(90, 99)
    print(avg1)

    help(func_with_return.my_headline)
    head1: str = "python has concurred the world"
    print(func_with_return.my_headline(head1))

    con_res = func_with_return.concat_list([9, 8, 7], [6, 5, 4, 3], [2, 1])
    print(con_res)
    print("length: ", len(con_res))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
