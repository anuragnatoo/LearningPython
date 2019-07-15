#Number of occurences
test = [45,55,45,65,10,2,5,10,1,2,5,10]
def numberof(list,ele):
    count = 0
    for e in list:
        if e == ele:
            count += 1
    return count
for i in test:
    print(i,"occurs",numberof(test,i),"times")
# Reversing a string
def reversestring(string1):
    result = ""
    for c in string1:
        result = c + result
    return result
print(reversestring("ABCDEFGH"))
print(reversestring("HELLO"))
#Sum of elements in list
def sumfunction(list):
    sum = 0
    for a in list:
        sum = sum + a
    return sum
print(sumfunction([1,23,45,68,10]))
# Max element in list
def maxelement(list):
    max = list[0]
    for i in list :
        if i > max:
            max = i
    return max
print(maxelement([1,23,45,68,10]))
# Number of words in input string
def numberofwords(input):
    count = 1
    if len(input) == 0:
        return 0
    for i in input:
        if i == " ":
            count += 1
    if input[len(input)-1] == " ":
        count -= 1
    return count
print(numberofwords("Hello! Lets count the number of string here"))
print(numberofwords(""))
#Isprefix of another
def isprefixof(input,prefix):
    if len(input) < len(prefix):
        return False
    i = 0
    while i < len(prefix):
        if prefix[i] != input[i]:
            return False
        i += 1
    return True
print(isprefixof("Hello","He"))
print(isprefixof("Hello","Hell"))
print(isprefixof("Hello",""))
print(isprefixof("Hello","olleh"))