#multilevel inheritence 
class parent:
    a=10

class child(parent):
    b=20
    def display(self,age):
        self.age=age

class child_child(child):
    def display(self):
        print(self.a + self.b)
    

obj1=child()
obj1.display(7)
obj2=child()
obj2.display(14)

'''for name in parent.__dict__:
    print (name)'''


print(obj1.__dict__)
print(obj2.__dict__)