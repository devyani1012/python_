import datetime
from grade import calculate_grade 

class student:
    def __init__(self,name,rollno,marks,addmission_date):
        self.name = name
        self.rollno = rollno
        self.addmission_date = addmission_date
        self.set_marks(marks)


    def get_marks(self):
        return self.__marks

    
    def set_marks(self,marks):
        if marks < 0 or marks > 100:
            raise ValueError("Marks should be between 0 and 100")
        self.__marks = marks

    def calculate_grade(self):
        return calculate_grade(self.__marks)
        

    def display(self):
        print("name of student is:",self.name)
        print("rollno of student is:",self.rollno)
        print("marks of student is:",self.get_marks())
        print("grade of student is:",self.calculate_grade())
        print("addmission date of student is:",self.addmission_date)


name=input("enter name of student:")
rollno=input("enter rollno of student: ")
marks=int(input("enter marks of student: "))
addmission_date=datetime.date.today()

st=student(name,rollno,marks,addmission_date)
st.display()