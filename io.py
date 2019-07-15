# Python Input/Output
#file1 = open("testfile.txt","xt")
#file1.write("123")
#file2 = open("testfile.txt","w")
#file2.write("404\n")
#file2.write("Not Found")
#file2=open("testfile.txt","a")
#file2.write("\nI'm Still learning")
#file1.close()
#file2=open("filename.txt","r")
#print(file2.readline())
#print(file2.readline())
#print(file2.readline())
#print(file2.readline())
#for var in file2:
#   print(var)
'''
file2 = open("testfile2.txt","xb")
arr = 45
binary_format = bytes(arr)
file2.write(binary_format)
file2.close()
'''
file2 = open("testfile2.txt","xt")
file2.write("abcdefg")
file2.close()
import os
#os.remove("testfile.txt")
if os.path.exists("testfile2.txt"):
    os.remove("testfile2.txt")
    print('File succesfully removed')
else:
    print("File doesnt exist so it cant be removed")
os.rmdir("testdir")