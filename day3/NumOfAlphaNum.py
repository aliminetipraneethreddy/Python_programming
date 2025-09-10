def NumOfAlpha(s1):
    ca=0
    cn=0
    cs=0
    for char in s1:
        if( char.isalpha()):
            ca+=1
        elif(char.isdigit()):
            cn+=1
        else:
            cs+=1
    print(f"alpha->{ca}\n num->{cn}\nSpecial Symbol->{cs}")
s1="Praneeth69**Santhoshi"
NumOfAlpha(s1)