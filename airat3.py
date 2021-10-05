if __name__ == '__main__':
    print("здравствуйте")
    num_1 = int(input("1"))
    num_2 = int(input("2"))
    znak = input("-")
    if znak == '+':
        print(num_2 + num_1)
    elif znak == '-':
        print(num_2 - num_1)
    elif znak == '*':
        print(num_2 * num_1)
    elif znak == '/':
        print(num_2 / num_1)
    else:
        print("ты ошибся")

