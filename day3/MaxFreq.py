def Occurence(s1):
    visited=[]
    result=[]
    result1=[]
    for char in s1:
        if char not in visited:
            n=char
            count=0
            for char1 in s1:
                if n==char1:
                    count+=1
            #print(f"{char}{count},end=''")
            result .append( f"{count}")
            result1.append(char)
            visited.append(char)
    num1=max(result)
    index1=result.index(num1)
    print(f"{result1[index1]}{num1}")
    
s1="smtsrisanthoshisraneethreddy"
Occurence(s1)
                