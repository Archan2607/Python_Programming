"""

Remove Duplicate Charachters

"""

def RemoveDuplicate(s):
    k=set(s)
    for i in k:
        print(i,end="")

s1=input()
RemoveDuplicate(s1)
