'''
def examplefunc(arg1="default gets printed"):
    print("Example!",arg1)
examplefunc("Hey!")
examplefunc("How r u?")
examplefunc()

def example2():
    return 10
print(example2())
'''
#Recursion
def factorial(n):
    if n==1:
        return 1
    else:
        print("Look at me running!")
        return n*factorial(n-1)

def justanotherfunction():
    print("Just another print statement!")
