import re


class ExtractTime:
    """ Extract time from string


    """

    def __init__(self,string):
        self.DAY_NAME = ['дня','ночи']
        self.arr = []
        for i in range(len(string.split())):
            elem = string.split()[i]
            if re.match(r'(?:\d{1,2}:\d{2}|\d{1,2})', elem):
                if i+1 != len(string.split()) and string.split()[i+1] in self.DAY_NAME:
                    arr[i]




    def __iter__(self):
        self.cur_iter = 0
        return self

    def __next__(self):
        if self.cur_iter >= len(self.arr):
            raise StopIteration
        self.cur_iter += 1
        return self.arr[self.cur_iter - 1]


if __name__ == '__main__':
    UserInput = input()
    timer = ExtractTime(UserInput)
    for time in timer:
        print(time)
