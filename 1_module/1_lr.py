from typing import Union
from math import sin

def first_task():
    name: str = input("Input your name: ")
    age: str = input("Input yout age: ")
    place_residence: str = input("Input your place the residence: ")

    print("\nName:", name, "age:", age, "place:", place_residence)

def second_task():
    var_int: Union[int, float] = 0
    var_float: float = 0.0

    var_int = int(input("Input the value of integer variable: "))
    var_float = float(input("Input the value of float variable: "))

    print("Type of var_int is", type(var_int), "Type of var_float is", type(var_float))

    var_int = float(var_int)

    print("Type of var_int is", type(var_int))

    var_int = int(var_int)

    print("Type of var_int is", type(var_int))

    n: int = int(input("Input the number digits: "))
    str_var_float = str(var_float)
    str_var_float_i_dot = str_var_float.find(".")

    print(str_var_float[0 : str_var_float_i_dot], str_var_float[str_var_float_i_dot + 1 :])

def third_task():
    def f(x: Union[int, float]) -> Union[int, float]:
        return x**3 + 5 * x**2 + x - 10 * sin(5 * x) - 1

    x: Union[str, int, float] = input("Input the value of variable 'x': ")
    
    x = float(x) if "." in x else int(x)

    print(f(x))

if __name__ == "__main__":
    first_task()
    second_task()
    third_task()