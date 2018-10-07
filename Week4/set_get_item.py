class Arr:
    def __init__(self, name):
        self.name = name
        return

    def __getitem__(self, item):
        return self.name

    def __setitem__(self, key, value):
        self.name += str(key) + '-' + str(value)
        return


if __name__ == '__main__':
    a = Arr("Test")
    print(a.__getitem__(566))
    a.__setitem__('324', 234)
    print(a.__getitem__(234))

