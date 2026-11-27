try:
    num=int(input("enter a no:"))
    result=100/num
except ZeroDivisionError:
    print("number connot be zero")
else:
    print("result",result)        