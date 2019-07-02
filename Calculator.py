""""
print("************WITHOUT IF*************")
print("Hello! Welcome to my Calculator!")
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
add = num1+num2
sub = num1-num2
mult = num1*num2
div = num1/num2
print("Addition of two numbers gives", add)
print("Subtraction of two numbers gives", sub)
print("Multiplication of two numbers gives", mult)
print("Division of two numbers is", div)
"""
print("*************WITH CONDITIONS*********")
while True:
	print("Please Enter the operation you want to perfrom!")
	print("1---For Addition")
	print("2---For Subtraction")
	print("3---For Multiplication")
	print("4---For Division")
	print("5---To Quit")
	ans = int(input())
	if ans == 1:
		print("Please enter the numbers you want to add!")
		var1 = int(input("First Number goes here :"))
		var2 = int(input("Second Number goes here :"))
		print(var1+var2)
	elif ans == 2:
		print("Please enter the numbers you want to subtract!")
		var1 = int(input("First Number goes here :"))
		var2 = int(input("Second Number goes here :"))
		print(var1-var2)
	elif ans == 3:
		print("Please enter the numbers you want to multiply!")
		var1 = int(input("First Number goes here :"))
		var2 = int(input("Second Number goes here :"))
		print(var1*var2)
	elif ans == 4:
		print("Please enter the numbers you want to divide!")
		var1 = int(input("First Number goes here :"))
		var2 = int(input("Second Number goes here :"))
		try:
			print(var1/var2)
		except:
			print("Error! You Cannot Divide by Zero")
	elif ans == 5:
		break
print("Thanks For using this Calculator")