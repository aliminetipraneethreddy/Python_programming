def SetOperation(l1,l2,l3):
    s1=set()
    for i in l1:
        s1.add(i)
    for i in l2:
        s1.add(i)
    for i in l3:
        s1.add(i)
        
    print(s1)
    print(len(s1))
    count=0
    for i in s1:
        if i in l1 and i in l2 and i in l3:
            count+=1
    print(count)
l1=["apdd@.com","apdd1@.com","apd@.com"]
l2=["apdd1@.com","apd2d@.com","apdd@.com"]
l3=["apdd@.com","apd2d@.com","apdd1@.com"]
SetOperation(l1,l2,l3)
    