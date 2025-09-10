def NumOfVowels(s1):
    a=['A','E','I','O','U','a','e','i','o','u']
    v,c=0,0
    for char in s1:
        if char.isalpha():
            if char in a:
                v+=1
            else:
                c+=1
    print(f"vowels->{v}\nconsonents->{c}")
s1="Praneeth69Santhoshi"
NumOfVowels(s1)
        