from random import randint
a = 0
b = 100
print(f"Загадай число от {a} до {b} я попробую угадать!")
tryes = 1
again = True
while again:
    g = randint(a, b)
    if a == b:
        print(f"\033[38;2;0;255;0mВаше число - {a}!\033[0m")
        print(f"\033[38;2;0;255;0mЯ угадал за {tryes} попыток!\033[0m")
        print("\033[38;2;180;130;255mХотите ли попробовать еще раз?\033[0m")
        while True:
            agan = input()
            if agan.lower() == "да" or agan.lower() == "lf":
                a = 0
                b = 100
                tryes = 1
                break
            elif agan.lower() == "нет" or agan.lower() == "ytn":
                again = False
                break
            else:
                print("\033[38;2;255;80;80mНе совсем вас понял, попробуйте еще раз!\033[0m")
        continue
    print(f"\033[38;2;0;255;255mДумаю вы загадали число {g} скажи больше или меньше или я угадал?\033[0m")

    while True:
        c = input("\033[38;2;255;150;180mНапишите больше, меньше или оно: \033[0m")
        if "больше" in c.lower():
            a = g + 1
            tryes += 1
            break
        elif "меньше" in c.lower():
            b = g - 1
            tryes += 1
            break
        elif "оно" in c.lower():
            a = g
            b = g
            break
        else:
            print("\033[38;2;255;80;80mНе совсем вас понял, попробуйте еще раз!\033[0m")

