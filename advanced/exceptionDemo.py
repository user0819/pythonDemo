def spam():
    raise Exception('throw new exception')


if __name__ == '__main__':
    try:
        spam()
    except Exception as error:
        print(error)
