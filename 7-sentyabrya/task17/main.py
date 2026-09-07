class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if type(self.a) not in (int, float) or type(self.b) not in (int, float) or type(self.c) not in (int, float):
            return 1
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return 1
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return 2
        return 3
a, b, c = input().split()
try:
    a = int(a)
    b = int(b)
    c = int(c)
except:
    pass 
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())