class A:
    def intro(self):
        return "Im A"

class B(A):
    def intro(self):
        return "Im B"

class C(A):
    pass

class D(B, C):
    pass

a = A()
b = B()
c = C()
d = D()

print(a.intro())
print(b.intro())
print(c.intro())
print(d.intro())
