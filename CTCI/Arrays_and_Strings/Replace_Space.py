"""

Write a method to replace all spaces in a string with ‘%20’.

"""

def checkspace(s):
    sr = ""
    for i in s:
        if i == " ":
            sr += "%20"  
        else:
            sr += i 
    return sr

s1 = input()
print(checkspace(s1))
