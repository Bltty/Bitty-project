p = ("-------------------------------")
i = ("Kalkulačka delux edition xd")
b = ("------------------------------")

print (p)
print (i)
print (b)

while True:
    m = int(input("Zadejte kolik čísel chcete vypočítat: "))

    if m == 2:
        try:
            c = int(input("Zadejte číslo s kterým chcete počítat: "))
            d = int(input("Zadejte číslo s kterým chcete počítat: "))
            r = str(input("zadejte hodnutu kterou chcete počítat: "))
            if r == "+":
                print ("Váš výsledek je: ", c+d)
            if r == "-":
                print ("Váš výsledek je: ", c-d)    
            if r == "*":
                print ("Váš výsledek je: ", c*d)    
            if r == "/":
                print ("Váš výsledek je: ", c/d)
        except SyntaxError:
                 print("zadejte platní symbol")
    if m == 3:
        try:
            c= int(input("Zadejte číslo s kterým chcete počítat: "))
            p = int(input("Zadejte číslo s kterým chcete pracovat: "))
            d = int(input("Zadejte číslo s kterým chcete počítat: "))
            r = str(input("zadejte hodnutu kterou chcete počítat: "))   
            if r == "+":
                print ("Váš výsledek je: ", c+p+d)
            if r == "-":
                print ("Váš výsledek je: ", c-p-d)
            if r == "*":
                print ("Váš výsledek je: ", c*p*d)
            if r == "/":
                print ("Váš výsledek je: ", c/p*d)
        except SyntaxError:
            print("Zadejte platní symbol")
    if m == 4:
        try:
        
            p = int(input("Zadejte číslo s kterým chcete počítat: "))
            c = int(input("Zadejte číslo s kterým chcete počítat: "))
            d = int(input("Zadejte číslo s kterým chcete počítat: "))
            u = int(input("zadejte číslo s kterým chcete počítat: "))
            r = str(input("zadejte hodnutu kterou chcete počítat: "))
            if r == "+":
                print ("Váš výsledek je: ", p+c+d+u)    
            if r == "-":
                print ("Váš výsledek je: ", p-c-d-u)    
            if r == "*":
                print ("Váš výsledek je: ", p*c*d*u)    
            if r == "/":
                print ("Váš výsledek je: ", p/c/d/u/r)  
        except SyntaxError:
            print("zadejte platní symbol")
    if m == 5:
        try:
        
            l = int(input("Zadejte číslo s kterým chcete počítat: "))
            p = int(input("Zadejte číslo s kterým chcete počítat: "))
            c = int(input("Zadejte číslo s kterým chcete počítat: "))
            d = int(input("Zadejte číslo s kterým chcete počítat: "))
            u = int(input("zadejte číslo s kterým chcete počítat: "))
            r = str(input("zadejte hodnutu kterou chcete počítat: "))
            if r == "+":
                print ("Váš výsledek je: ", l+p+c+d+u)  
            if r == "-":
                print ("Váš výsledek je: ", l-p-c-d-u)  
            if r == "*":
                print ("Váš výsledek je: ", l*p*c*d*u)  
            if r == "/":
                print ("Váš výsledek je: ", l/p/c/d/u/r)    
        except SyntaxError:
            print("zadejte platní symbol")  
    if m == 6:
        try:
        
            l = int(input("Zadejte číslo s kterým chcete počítat: "))
            p = int(input("Zadejte číslo s kterým chcete počítat: "))
            c = int(input("Zadejte číslo s kterým chcete počítat: "))
            d = int(input("Zadejte číslo s kterým chcete počítat: "))
            u = int(input("Zadejte číslo s kterým chcete počítat: "))
            y = int(input("Zadejte číslo s kterým chcete počítat: "))
            r = str(input("z6adejte hodnutu kterou chcete počítat: "))
            if r == "+":
                print ("Váš výsledek je: ", l+p+c+d+u+y)    
            if r == "-":
                print ("Váš výsledek je: ", l-p-c-d-u-y)    
            if r == "*":
                print ("Váš výsledek je: ", l*p*c*d*u*y)    
            if r == "/":
                print ("Váš výsledek je: ", l/p/c/d/u/r/y)  
        except SyntaxError:
            print("zadejte platní symbol")  
    print ("-------------------------------------------------------------------------------------")
    print ("děkujeme za využitý naší kalkulačky nezapomeňte nám dát 5 hvezdiček v appstore xd ")

