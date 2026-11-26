class file:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, "w")
        print("file opened")
    def write_data(self, data):
        self.file.write(data)

    def __del__(self):
        self.file.close()
        print("file closed")

f1 = file("myfile.txt")
f1.write_data("hello world")

del f1

with open("myfile.txt", "r") as f:
    print(f.read())