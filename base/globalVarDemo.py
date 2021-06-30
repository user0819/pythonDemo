name = 'global name'


def test_global():
    global name
    name = 'inner name'
    print(name)


if __name__ == '__main__':
    print(name)
    test_global()
    print(name)

