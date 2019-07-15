#Lists
listVar = ["apple",'google','alphabet']
print(listVar)
listVar[0]='404'
print(listVar)
#Tuples
tupleVar = ('Apple', 'Google','Alphabet')
print(tupleVar)
# tupleVar[0]='Apple'
# Sets
setVar={'1','2','4','2'}
print(setVar)
print(len(setVar))
# List Operations
if "google" in listVar:
    print("Yes it's present")
else:
    print("Sorry! I am not available")
print(len(listVar))
listVar.append(4)
print(listVar)
print(len(listVar))
listVar.insert(1,35)
print(listVar)
print(len(listVar))
listVar.remove(35)
print(listVar)
print(len(listVar))
del listVar[0]
print(listVar)
print(len(listVar))
listVar.clear()
print(listVar)
print(len(listVar))
listVar.insert(1,"Happy")
print(listVar)
print(len(listVar))
tupleVar=('apple','google','samsung','oneplus')
if 'google' in tupleVar:
    print(True)
else:
    print(False)
print(tupleVar)
print(len(tupleVar))
index1 = listVar.index("Happy")
print(index1)
#Set Operations
myset1={'1','2','3'}
myset2={'abc','def','ghi'}
result= myset1.union(myset2)
print(result)
print(len(result))
result = myset1.union(myset1)
print(result)
print(len(result))
result=myset1.intersection(myset2)
print(result)
print(len(result))
result=myset1.intersection(myset1)
print(result)
print(len(result))
tuple2=()
print(tuple2)
print(len(tuple2))
print(setVar)
setVar.add('1')
print(setVar)
#Loops
enjoy=['prime','netflix','hotstar']
print(enjoy)
for var1 in enjoy:
    print(var1.upper())
for var2 in enjoy[2]:
    print(var2)
print(var1)
print(var2)
listVar2=[45,56,64,36,44,20]
print(listVar2)
## Dictionaries
items={
    "key" : "value",
    "Brand" : "Audi",
    "Model" : "A4",
    "Year" : 2020
}
print(items)
temp1=items["Brand"]
temp2=items.get("Year")
print(temp1)
print(temp2)
for x in items:
    print(x)
print()
for x in items.values():
    print(x)
print()
for x in items:
    print(items[x])
print()
for x,y in items.items():
    print(x,y)
print()
if "Brand" in items:
    print("Yes its there")
else:
    print("Not Found")
if "Brand" in items.values():
    print("Yes its there")
else:
    print("Not Found")
items["Price"] = "340000"
print(items)
del items["key"]
print(items)
i = 0
while i < 7:
    if i == 2 or i == 3:
        continue
    if i >= 5:
        break
    print(i)
    i += 1