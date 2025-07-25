class Student:
    name="mahi"
    age=21
    def display(self,name,age):
        
        print(name,"\n",age)
        print(self.name,"\n",self.age)


student1 = Student()

student1.display(input("Enter name"),int(input("Enter age")))





