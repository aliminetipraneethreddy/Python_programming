def CountEvOdd(l1):
    count1=0
    count2=0
    for i in range(0,len(l1)):
        if l1[i]%2==0:
            count1+=1
        else:
            count2+=1
    print(f"Even:{count1}Odd:{count2}")
l1=[2,21,3,342,44,3,451,69,45,78]
CountEvOdd(l1)