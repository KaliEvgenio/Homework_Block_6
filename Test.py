class A:
    def __init__(self):
        self.name='Object A'

class B(A):
    def __init__(self):
        self.name='Object B'

x=A()
y=B()
print(x.name,'isinstance(x,A)=',isinstance(x,A))
print(x.name,'isinstance(x,B)=',isinstance(x,B))
print(y.name,'isinstance(y,A)=',isinstance(y,A))
print(y.name,'isinstance(y,B)=',isinstance(y,B))