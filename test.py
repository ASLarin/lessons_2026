def print_signature():
    """simple function for print signature"""
    print("bmstu")

def simple_sum(a, b):
    """simple function for summary a and b"""
    return a + b

def main():
    """fucntion activate all sub_functions"""
    print(simple_sum(1, 2))
    print_signature()

if __name__=='__main__': 
    main()


def func_for_py_3_6():
    name = "World" # работает в 3.6 и выше в 3.5 вызовет ошибку синтаксиса
    print(f"Hello, {name}!")


def func_for_py_3_10(data: int | str): # 
    print(data)

a = []
func_for_py_3_10(a)

x = [1, 10, 100, 1000]

print(sum(x))
