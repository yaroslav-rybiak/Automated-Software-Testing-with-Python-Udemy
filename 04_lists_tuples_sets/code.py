myList = ["a", "b", "c", "c"]
myList.append("d")
myList.insert(1, "v")
myList.pop(0)
myList[2] = "o"
myList[3] = "i"
myList.remove("b")
print(myList)
print(myList[0])

myTuple = ("a", "b", "c", "c")
#can not be modified
print(myTuple)

mySet = {"a", "b", "c", "c"}
#can't have duplicates
#don't have order
mySet.add("c")
print(mySet)