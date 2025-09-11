try:
    num=int(input("Enter NUmerator "))
    den=int(input("Enter Denominator"))
    print(num//den)
except ZeroDivisionError:
    print("Den is zero")
else:
    print("Ntr is 6ft")
finally:
    print("ntr is lilput")