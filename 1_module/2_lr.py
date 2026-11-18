from typing import Union

def first_task():
    s: str = input("In: ")

    print(f"Out: ({s[0: 3]}) {s[3: 6]}-{s[6 :]}")

def second_task(s: str):   
    print("In: ")
 
    list_format_sub_s: list[str] = [chr(ord(sub_s) + 1) for sub_s in s]
    format_s: str = "".join(list_format_sub_s)

    print("Out: ", format_s)

def third_task(marks: str):
    print("In: ")

    list_marks: list[int] = [int(mark) for mark in marks.split(" ")]

    print("Out: ", sum(list_marks) / len(list_marks), max(list_marks), min(list_marks)) 

def fourth_task(list_s: list[str]):
    print("In: ")

    list_square_root: list[Union[list, float]] = [round(num**0.5, 2) for num in [int(s) for s in list_s]]

    print("Out: ", list_square_root)

if __name__ == "__main__":
    first_task()
    second_task("sdflke3j")
    third_task("1 98 33 93 6")
    fourth_task(["12", "923", "144"])