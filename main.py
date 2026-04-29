def add(a, b):
    return a + b

print(add(5, 5 ))

def subtract(a, b):
    return a - b

print(subtract(5, 5))

def multiply(a, b):
    print(a * b)


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return add(self.a, self.b)

obj = Math(5, 5)
print(obj.add())
