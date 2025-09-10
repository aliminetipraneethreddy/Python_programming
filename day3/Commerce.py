def discount(price,dis):
    return( price-price*(dis/100))
def addgst(price,gst=18):
    price+=price*(gst/100)
    return price
def invoice(cart,dis=0,gst=18):
    sum=0
    for i in cart:
        print(f"{i}:{cart[i]}")
        sum+=cart[i]
    sum=discount(sum,10)
    print(f"After {dis} {sum}")
    sum=addgst(sum,18)
    print("After {gst} {sum}")
    print("-------------------------------------")
    print("Thank U  Visit again")


