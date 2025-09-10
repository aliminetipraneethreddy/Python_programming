def RemoveEle(l1,pos):
    if len(l1)<=pos:
        return 
    for i in range(pos,len(l1)-1):
        l1[i]=l1[i+1]
    return l1
l1=[2,21,3,342,44,3,451,69,45,78]
print(RemoveEle(l1,1))