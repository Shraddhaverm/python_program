class A:
    def __repr__(self):
        return "1"
class B(A):
    def __repr__(self):
        return "2"
class C(B):
    def __repr__(self):
        return "3"
o1 = A()
o2 = B()
o3 = C()
print('obj1', 'obj2', 'obj3')


# questions
class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return 1
    def __eq__(self, other):
        return self.x * self.y == other.x * other.y
obj1 = A(5, 2)
obj2 = A(2, 5)
print(obj1 == obj2)
# edd
f = foo()
format(f)
#
class A():
    pass
class B():
    pass
class C(A,B):
    pass

####
class A:
     def __init__(self):
         self.__i = 1
         self.j = 5
 
     def display(self):
         print(self.__i, self.j)
class B(A):
     def __init__(self):
         super().__init__()
         self.__i = 2
         self.j = 7  
c = B()
c.display()