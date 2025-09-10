def OccurenceChar(s1,c):
    count=0
    for char in s1:
        if c==char:
            count+=1
    return count
s1="SmtSri Santhoshi Praneeth Reddy"
print(OccurenceChar(s1,'s'))
