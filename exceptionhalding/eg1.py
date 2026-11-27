try:
    num=int(input("enter a no:"))
    result=100/num
except(ValueError, ZeroDivisionError):
    print("invalid input ")
      