num = [1, 4, 5, 7, 8]

# print(num)
# for str in num:
#      print(str, end =" ")

# num[3] = 10
# print(num)

for index in range(len(num)):
    str = num[index] * 2
    print(str
          )

sentence = "I am abir yusuf"
str = (sentence.split())

# I can not upper without indicating position, so need to use for loop with range and len
# for index in range(len(sentence)):
#     str = sentence[index].upper()
#     print(str, end=" ")

# Searching a list
aList = [1, 3, 10, 4, 5, 6, 7, 2]
# I can use the in operator to detect the presence or absence of a given element:
print(3 in aList)
print(aList.sort())
target = 5
if target in aList:
    print("IN LIST: ", aList.index(target))
else:
    print("Not in list")
data = [5, 3, 7]
print(tuple(data))
# Assume that the variable data refers to the list [5, 3, 7]. Write the values of the following expressions:


first = [10, 20, 30, 40]

second = first

third = []

# for ele in first:
#     third.append(ele)
#     print(ele, end=" ")
#
#     print(first[1])
third = list(first)
print(third)

