def CompareCat(s1,s2):
    if s1 is s2:
        print("Both are same")
    elif length(s1)>length(s2):
        print("S1 is greater than s2")
    else:
        print("s2 is greater than s1")
    s=s1+s2
    print(s)
def length(s1):
    count=0
    for char in s1:
        count+=1
    return count

s1="Santhoshi"
s2="Praneeth"
CompareCat(s1,s2)