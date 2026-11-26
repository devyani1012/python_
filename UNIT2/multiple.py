class student:
    def __init__(self):
        self.__name = ""
        self.__rollno = 0
        self.__marks = ""

        #setter methods
    def set_data(self,name,rollno,marks):
        self.__name = name
        self.__rollno = rollno
        if 0<=marks>=100:
            self.__marks = marks

        else:    
            print("invalid marks")


        #getter methods
    def get_data(self):
        print("name  : ",self.__name)
        print("rollno  : ",self.__rollno)
        print("marks is : ",self.__marks)

s1=student()
name=input("enter name : ")
rollno=int(input("enter rollno : "))
marks=float(input("enter marks : "))
s1.set_data(name,rollno,marks)
print("\n student details are : ")
s1.get_data()