"""
Checking whether two strings are anagrams or not

"""

def Is_Anagram(s1,s2):
    a1 = list() 
    a2 = list()
    if (len(s1)!=len(s2)) == 1:
        print(False)
    else:
        k=len(s1)
        c=0
        d=0
        for i in range(k):
            if (a1[i] == a2[i]) == 1:
                c=c+1
            else:
                d=d+1
        a1 = sorted(s1)
        a2 = sorted(s2)
        if(d>0):
            print(False)
        else:
            print(True)
                
a=input()
b=input()

b1=a.lower()
b2=b.lower()

Is_Anagram(b1,b2)
        
