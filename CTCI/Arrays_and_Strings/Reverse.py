"""

Write code to reverse a String. 

"""

def reverse(s):
    sr = ""
    for i in s:
        sr = i + sr
    return sr
    
s1=input()
print(reverse(s1))
    
