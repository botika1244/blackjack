import random
import time

dealer = 0
jatekosszam = 0
dealerlapjai = []
jatekos = 0
jatekoslapjai = []
jatekos2 = 0
jatekos2lapjai = []
huzas = 0
megy = 1

def kiiras(opcio):
    global dealer
    global jatekos
    global jatekos2
    global dealerlapjai
    global jatekoslapjai
    global jatekos2lapjai

    if opcio == "dealer":
        print(f"Dealer lapjai🐱‍👤: lapok:{dealerlapjai} ({dealer}) \nJátékos😎: lapok:{jatekoslapjai} ({jatekos})\n")
    elif opcio == "jatekos":
        print(f"Játékos 1😎: lapok:{jatekoslapjai} ({jatekos}) \nJátékos 2😎: lapok:{jatekos2lapjai} ({jatekos2})\n")

def huz(ki):
    global huzas
    global jatekos
    global jatekos2
    global dealer
    huzas = random.randint(2,11)
    if ki == "jatekos":
        jatekos += huzas
        jatekoslapjai.append(huzas)
    if ki == "dealer":
        dealer += huzas
        dealerlapjai.append(huzas)
    if ki == "jatekos2":
        jatekos2 += huzas
        jatekos2lapjai.append(huzas)

def dontes(ki):
    global megy
    global jatekos
    global jatekosszam
    global jatekos2

    if ki == "jatekos":
        valasz = input("Szeretnél kártyát felhúzni? [i/n]:")
        print("\n\n\n\n\n\n\n")
        if valasz == "n":
            megy = 0
            return
        if valasz == "i":
            huz("jatekos")
        if jatekos > 21:
            megy = 0
        elif jatekosszam == 1:
            kiiras("dealer")
        else:
            kiiras("jatekos")

    if ki == "jatekos2":
        valasz = input("Szeretnél kártyát felhúzni? [i/n]:")
        print("\n\n\n\n\n\n\n")
        if valasz == "i":
            huz("jatekos2")
        if valasz == "n":
            megy = 0
            return
        if jatekos2 > 21:
            megy = 0
        kiiras("jatekos")

print("Üdvözöllek, ez itt egy BlackJack játék!")
jatekosszam = int(input("Hány játékos fog játszani? [1 / 2]:"))

if jatekosszam == 1:
    print("A dealer és a játékos is húz kettő-kettő lapot. \n")
    i = 2
    while i > 0:
        huz("dealer")
        huz("jatekos")
        i = i - 1
    kiiras("dealer")
    while megy == 1:
        dontes("jatekos")
    if megy == 0:
        kiiras("dealer")
        time.sleep(1)
        if jatekos <= 21:
            while dealer <= 16:
                huz("dealer")
                print("Húz a dealer...")
                time.sleep(3)
                print("\n\n\n\n\n\n\n")
                kiiras("dealer")
            if dealer > jatekos and dealer <= 21:
                print("❌Vesztettél!❌")
            elif dealer == jatekos:
                print("Döntetlen!")
            else:
                print("💲Nyertél!💲")
        else:
            print("❌Vesztettél, mivel átlépted a 21-et!❌")
else:
    print("Mindkét játékos húz kettő-kettő lapot. \n")
    i = 2
    while i > 0:
        huz("jatekos")
        huz("jatekos2")
        i = i - 1
    kiiras("jatekos")
    while megy == 1:
        dontes("jatekos")
    print("Most a második játékos jön...")
    megy = 1
    time.sleep(1)
    kiiras("jatekos")
    while megy == 1:
        dontes("jatekos2")

if jatekosszam == 2:
    if jatekos <= 21 and jatekos2 <= 21:
        if jatekos > jatekos2:
            print("1️⃣Az első játékos nyert!1️⃣")
        elif jatekos < jatekos2:
            print("2️⃣A második játékos nyert!2️⃣")
        else:
            print("🔄Döntetlen!🔄")
    elif jatekos > 21 and jatekos2 > 21:
        print("🔄Döntetlen🔄")
        jatekosszam = 0
    elif jatekos > 21:
        print("2️⃣Második játékos nyert!2️⃣")
    elif jatekos2 > 21:
        print("1️⃣Első játékos nyert!1️⃣")
