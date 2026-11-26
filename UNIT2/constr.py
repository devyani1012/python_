class student:
    count=0
    def __init__(self,name):
        self.name=name
        student.count+=1
        print("student created")

    def get_data(self):
        student.count-=1    
        print("student del")

    @classmethod
    def get_count(cls):
        print("total students : ",cls.count)

s1=student("tommy")
s1=student("jerry")
s1=student("mickey")

s1.get_data()

s1.get_count()