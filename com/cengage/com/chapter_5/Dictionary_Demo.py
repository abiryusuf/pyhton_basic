# A Python dictionary is written as a sequence of key/value
# pairs separated by commas. These pairs are sometimes
# called entries. The entire sequence of entries is enclosed in
# curly braces ({ and }). A colon (:) separates a key and its value.

info = {
    "Name": "Abir",
    "Age": 18,
    "Location": "NY"
}
print(info)
# change the value by using key
info["Name"] = "yusuf"

# adding items
info["Phone"] = 9292615225
print(info)

# Accessing Items
print(info["Name"])
print(info.get("Age"))

print("*****LOOP*****")
for str, str1 in info.items():
    print(str, str1, end=", ")

for x in info:
    print(info[x])

# check the the value if inside the object
print("**** check the value")
if "Location" in info:
    print("yes")
else:
    print("No")

grades = {90: 'A', 80: 'B', 70: "C"}

s = list(grades.items())
print(s)
for (K, V) in grades.items():
    print(K, V)
#5-3f, 5-3g