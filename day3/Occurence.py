def Occurence(s1):
    visited=[]
    result=""
    for char in s1:
        if char not in visited:
            n=char
            count=0
            for char1 in s1:
                if n==char1:
                    count+=1
            #print(f"{char}{count},end=''")
            result += f"{char}{count}"

            visited.append(char)
    print(result)
s1="SmtSriSanthoshiPraneethReddy"
Occurence(s1)
                