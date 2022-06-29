p = ("-------------------------------")
i = ("Kalkulačka delux edition xd")
b = ("------------------------------")

print (p)
print (i)
print (b)

while True:
    try:
        m = int(input("Zadejte kolik čísel chcete vypočítat: "))
        c = int(input("Zadejte číslo s kterým chcete počítat: "))
        d = int(input("Zadejte číslo s kterým chcete počítat: "))
        r = str(input("zadejte hodnutu kterou chcete počítat: "))

        if r == "+":
            print ("Váš výsledek je: ")
            print (c+d)
            
        if r == "-":
            print ("Váš výsledek je: ")
            print (c-d)
        
        if r == "*":
            print ("Váš výsledek je: ")
            print (c*d)
        
        if r == "/":
            print ("Váš výsledek je: ")
            print (c/d)

    

    except ValueError :
     Print("zadejte číslo nebo znamínko")

