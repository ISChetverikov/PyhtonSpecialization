import tempfile
import random
from os import path


class File:
    def __init__(self, path):
        self.path = path
        self.pos = 0
        return

    def read(self):
        f = open(self.path, 'r')
        text = f.read()
        f.close()
        return text

    def write(self, text):
        f = open(self.path, 'w')
        f.write(text)
        f.close()
        return

    def __add__(self, other):
        file_path = path.join(tempfile.gettempdir(), "res" + str(random.randint(0, 10000)) + ".txt")

        a = File(file_path)
        a.write(self.read() + other.read())

        return a

    def __str__(self):
        return self.path

    def __iter__(self):
        return self

    def __next__(self):
        f = open(self.path, 'r')
        f.seek(self.pos)

        line = f.readline()

        if not line:
            self.pos
            raise StopIteration

        self.pos = f.tell()
        f.close()
        return line.rstrip()


# a = File("a.txt")
# b = File("b.txt")
#
# for line in a+b:
#     print(line)


