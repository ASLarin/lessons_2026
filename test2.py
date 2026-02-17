import random
import math 

def years():
    name = input("Имя питомца")
    n = int(input("Сколько лет"))
    n = n * 12
    return n

def strings1():
    words = input().split()
    words.reverse()
    rev_words = "_".join(words)
    return rev_words 

def strings2():
    words = input().split()
    rev_words = "_".join(words[::-1])
    return rev_words 

def strings3():
   words = input().split()
   a, b, c = words.split()
   print(f"{c}_{b}_{a}")

def procent():
    sum = int(input())
    tea = int(input())
    return sum + ((sum * tea) / 100)

def area():
    R = int(input())
    r = int(input())
    return math.pi * (R**2 - r**2)

def pappers_please():
    age = int(input("Введите возраст: "))
    passport = input("Есть паспорт?").lower() == "да"
    invite = input("Есть пригласительный?").lower() == "да"
    if (age >= 18 and passport) or invite:
        print("Проходите")
    else:
        print("Вход воспрещён")

def names():
    full_name = input()
    length = len(full_name)
    f_name, l_name = full_name.split()
    p1 = l_name[:3].upper()
    p2 = f_name[:2].lower()
    nick = f"{p1}_{p2}{length}"
    return nick

def hashteg():
    text = input()
    print([w[1:].upper() for w in text.split() if w.startswith("#")][0])

def random_chill_number():
    secret = random.randint(1, 100)
    attempts = 5  
    print("угадай 1 до 100")
    while attempts > 0:
        print(f"Попыток left {attempts}")
        guess = int(input())
        if guess == secret:
            print("угадал")
            break 
        elif guess < secret:
            print("Больше")
        else:
            print("Меньше")
        attempts -= 1  
        if attempts == 0:
            print(f"Попыток нету {secret}")

def sum_of_number():
    num = int(input())
    sumk = 0
    while num > 0:
        sumk += num % 10
        num = num // 10
    print(sumk)


sum_of_number()

