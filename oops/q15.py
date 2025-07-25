class Student:
    def display(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        print("Step 1: Original Attributes")
        print("ID:", self.student_id)
        print("Name:", self.student_name)

class AddClass(Student):
    def display(self, student_class):
        super().display(101, "Mahi")
        self.student_class = student_class
        print("\nStep 2: After Adding 'student_class'")
        print("ID:", self.student_id)
        print("Name:", self.student_name)
        print("Class:", self.student_class)

class RemoveName(AddClass):
    def display(self):
        super().display("VII")
        del self.student_name  # Remove student_name attribute
        print("\nStep 3: After Removing 'student_name'")
        print("ID:", self.student_id)
        print("Class:", self.student_class)
        print("\nCurrent Attributes in Object:", self.__dict__)

# Object creation
obj1 = Student()
obj2 = AddClass()
obj3 = RemoveName()

print("MENU\n1. Original Attributes\n2. Add Class\n3. Remove Name")
choice = int(input("Enter Choice: "))

if choice == 1:
    obj1.display(101, "Mahi")
elif choice == 2:
    obj2.display("VII")
elif choice == 3:
    obj3.display()
