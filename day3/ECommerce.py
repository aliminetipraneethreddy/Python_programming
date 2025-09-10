l1=[]
print("1.Add a product to the cart.")
print("2.Remove a product from the cart ")
print("3.Search for a product in the cart ")
print("4.Display all products in the cart")
print("5.Show the total number of products in the cart")

while True:
    c1=int(input("Enter"))
    if c1==1:
        val=input("Enter Product")
        l1.append(val)
    elif c1==2:
        val=input("enter Product to be removed")
        if val in l1:
            l1.remove(val)
            print("Product removed")
    elif c1==3:
        val=input()
        if val in l1:
            print("Product available")
        else:
            print("Product is not available")
    elif c1==4:
        print(l1)
    elif c1==5:
        print("Total NUmber of Products",len(l1))
    elif c1==6:
        l1=sorted(l1)
        print("Sorted")
    elif c1==7:
        l1.clear()
        print(l1)
    else:
        break   

    

