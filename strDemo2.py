"""myLang = "I know {}".format("Python")
print(myLang)

myLang = "I know {2} {1}  {0}".format("Python","java","JS")
print(myLang)

myLang = "I know {p} {JS} {j} ".format(p = "Python", j="Java", JS = "Java Script")
print(myLang)

# -----------------
name = "Ezhil"
print(f"My name is {name}")
# or
print("My name is {}".format(name))

# indexing & slicing == == negative indexing(-1,-2.. right to left) and positive indexing(0,1..)
sent = "Python is very easy"
print(sent[0])
print(sent[-1])
print(sent[6])

print(sent[-3])



name = "MyNameIsEzhil"
print(name[8:])
print(name[8:12])

name = "pythonisveryeasy"
print(name[6:8])

print(name[0::2])
print(name[::3])
print(name[::-1])  # reverse
"""
# =================
#  List in python
# =================
list1 = [10,50,60,90]
print(list1)
print(type(list1))

list2 = ["ezhil", 10, 20, True]
print(list2)

print(len(list2))

list3 = list1 + list2
print(list3)

print(len(list3))

list4 = [23,45,67,88]
print(list4)

print(list4[0])
print(list4[-2])
# rint(list4[5])  # error


# slicing
print(list4[0:])
print(list4[1:3])

list4[0] = 77777
print(list4)

# append - append the value at the end of list
list4.append("test")
print(list4)

# insert

list4.insert(0,555)
print(list4)

list4.insert(3,999)
print(list4)

# pop - remove last element

lst1 = [12,89,78,90]
lst2 = ["ezhil","loki","python"]

lst1.extend(lst2)
print(lst1)

print(lst1.extend(list4))

list3 = "ezhil"
lst1.extend(list3)
print(lst1)

# pop
lst1.pop()
print(lst1)
lst2.pop()
print(lst2)

# remove - index value used to delete
lst2.remove("ezhil")
print(lst2)

# sort
list5 = [99,77,56,77,2,88,65,21,3,156]
list5.sort()
print(list5)


# reverse
list5.reverse()
print(list5)
list6 = ["ezhil", "loki", "sanji", "mahi"]
list6.reverse()
print(list6)









