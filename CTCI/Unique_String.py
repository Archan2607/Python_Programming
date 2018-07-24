"""
Implement an algorithm to determine if a string has all unique charachters

"""

def is_unique(s):
    return len(s) == len(set(s))


s1 = input()
s2=s1.lower()
print(is_unique(s2))
