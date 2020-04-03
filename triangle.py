print()
print()
print("       \\-----------------/       ")
print("        \\               /        ")
print("         \\             /         ")
print("          \\           /          ")
print("           \\         /           ")
print("            \\       /            ")
print("             \\     /             ")
print("              \\   /              ")
print("               \\ /               ")
print("                V                 ")
print("Benvenuto in Triangle!")
print()
print()


while True:
    print("Per il calcolo del Perimetro digita \"1\"")
    print("Per il calcolo dell'Area digita \"2\"")
    print("Per trovare un cateto digita \"3\"")
    print("Per uscire dal programma digita \"q\"")
    scelta = input("> ")

    if scelta == "q":
        break
    print()
    

    if scelta == "1":
        
        def PerimetroCalc ():
            c1 = input("Primo cateto> ")
            c2 = input("Secondo cateto> ")
            c3 = input("Terzo cateto> ")
            PerimetroRis = int(c1) + int(c2) + int(c3)
            print("\nPerimetro = " + str(PerimetroRis))
            print()
            print()
            return(PerimetroCalc)
        PerimetroCalc()

    elif scelta == "2":
        b = input("\nBase = ")
        h = input("Altezza = ")
        risultato = (int(b) * int(h)) / 2
        print("Risultato = " + str(risultato))

        print("\nVuoi calcolare anche il Perimetro? S/n")
        sceltaPA = input("\n> ")

        if sceltaPA == "S":

            def PerimetroCalc ():
                c1 = input("Primo cateto> ")
                c2 = input("Secondo cateto> ")
                c3 = input("Terzo cateto> ")
                PerimetroRis = int(c1) + int(c2) + int(c3)
                print("\nPerimetro = " + str(PerimetroRis))
                print()
                print()
                return(PerimetroCalc)
            PerimetroCalc()

        else:
            pass

    elif scelta == "3":
        
        print("\nBase \"b\"")
        print("Altezza \"h\"")
        print("Ipotenusa \"i\"")
        cateto_scelto = input("\nQuale cateto ti manca?")
        perimetro_da_cateto = input("\nPerimetro del triangolo> ")

        if cateto_scelto == "b":

            hCateto = input("\nAltezza> ")
            iCateto = input("Ipotenusa> ")
            brisultato = int(perimetro_da_cateto) - int(hCateto) - int(iCateto)
            print("\nb= " + str(brisultato))
            print()
            print()

        elif cateto_scelto == "h":

            bCateto = input("\nBase> ")
            iCateto = input("Ipotenusa> ")
            hrisultato = int(perimetro_da_cateto) - int(bCateto) - int(iCateto)
            print("\nh= " + str(hrisultato))
            print()
            print()

        elif cateto_scelto == "i":
            
            bCateto = input("\nBase> ")
            hCateto = input("Altezza> ")
            irisultato = int(perimetro_da_cateto) - int(bCateto) - int(hCateto)
            print("\nh= " + str(irisultato))
            print()
            print()