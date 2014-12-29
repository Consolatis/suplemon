

class Line:
    def __init__(self, data):
        self.data = data
        self.x_scroll = 0

    def __getitem__(self, i):
        return self.data[i]

    def __setitem__(self, i, v):
        self.data[i] = v

    def __str__(self):
        return self.data

    def __add__(self, other):
        return str(self) + other
    
    def __radd__(self, other):
        return other + str(self)

    def __len__(self):
        return len(self.data)

    def find(self, what):
        return self.data.find(what)

    def strip(self, *args):
        return self.data.strip(*args)
