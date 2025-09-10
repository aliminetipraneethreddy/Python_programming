def CountOfDup(l1):
    visited=[]
    num=0
    for i in range(len(l1)):
        num=l1[i]
        if num not in visited:
            visited.append(num)
    
    n1= len(l1)-len(visited)
    return n1
l1=[2,2,21,3,44,44,3,451,69,78]
print(CountOfDup(l1))