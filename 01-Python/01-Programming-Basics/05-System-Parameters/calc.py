# pylint: disable=missing-module-docstring,missing-function-docstring,eval-used
import sys


def main():
    """Implement the calculator"""
    my_list= sys.argv
    my_list[1]=int(my_list[1])
    my_list[3]=int(my_list[3])
    if my_list[2]== "+":
        return my_list[1] + my_list[3]
    if my_list[2]== "-":
        return my_list[1] - my_list[3]
    #if my_list[2]== "*":
    return my_list[1] * my_list[3]






if __name__ == "__main__":
    print(main())
