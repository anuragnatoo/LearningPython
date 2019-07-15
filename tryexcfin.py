try:
    print(var)
    f=open("input.txt","x")
    f.write("Hello!")
    f.close()
except NameError:
    print("Name Error")
except FileExistsError:
    print("File Already Exists")
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Zero Division Error"
n1=int(input())
n2=int(input())
result=divide(n1,n2)
print(result)