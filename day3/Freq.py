def FreqOfEle(l1): 
    num=0
    visited=[]
    for i in range(len(l1)):
        count=0
        num=l1[i]
        if num  not in visited:
            for j in range(len(l1)):
                if num==l1[j]:
                    count+=1
            print(f"{num}->{count}")
            visited.append(num)
l1=[2,2,21,3,342,44,3,451,69,45,78]
FreqOfEle(l1)
    