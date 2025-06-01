def check_type(arg):
    if type(arg) == str:
        return "Literature"
    elif type(arg) == int or type(arg) == float:
        return "Math"
    elif type(arg) == bool:
        return "Science"

print(check_type("hello"))
print(check_type(10))
print(check_type(3.14))
print(check_type(True))
