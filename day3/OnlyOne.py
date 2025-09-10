def SetOperation(l1,l2,l3):
    s1=set()
    s2=set()
    s3=set()
    
    for i in l1:
        s1.add(i)
    for i in l2:
        s2.add(i)
    for i in l3:
        s3.add(i)
    s4=set()
    s4=s1^s2
    s5=set()
    s5=s4^s3
    print(s5)

    print(s1)
    print(len(s1))
    count=0
    print(len(s1.intersection(s2)))
    
    print(len(s2.intersection(s3)))
    print(len(s3.intersection(s1)))
    

    

l1=["apdd@.com","apdd1@.com","apd@.com"]
l2=["apdd1@.com","apd2d@.com","apdd@.com"]
l3=["apdd@.com","apd2d@.com","apdd1@.com"]
SetOperation(l1,l2,l3)
