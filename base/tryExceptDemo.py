def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("error occur")
        return None


if __name__ == '__main__':
    print(division(10, 2))
    print(division(10, 5))

    print(division(10, 0))
    print(division(10, 1))
