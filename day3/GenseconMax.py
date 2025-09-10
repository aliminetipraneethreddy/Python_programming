def Gen2nd(l1):
    max1=l1[0]
    for i in range(1,len(l1)):
        if l1[i]>max1:
            max1=l1[i]
    l1.remove(max1)
    max1=l1[0]
    for i in range(1,len(l1)):
        if l1[i]>max1:
            max1=l1[i]
    return max1
l1=[1,2,34,5,5,4,43,44213,2233]
print(Gen2nd(l1))    

