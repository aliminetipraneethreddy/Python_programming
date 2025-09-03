cname=input("enter name")
id=int(input("Enter id"))
p,l=map(int,input("enter present and last").split())
if p<l:
    print("enter correctly")
    exit

print("Customer details")
print(cname,"\t",id,"\t")
print("BILL=",(p-l)*3.80)