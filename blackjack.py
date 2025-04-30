import random
import time

dealer = 0
jatekos = 0
huzas = 0
megy = 1

def huz(ki):
    global huzas
    global jatekos
    global dealer
    huzas = random.randint(1,11)
    if ki == "jatekos":
        jatekos += huzas
    if ki == "dealer":
        dealer += huzas

def dontes():
    global megy
    global jatekos
    valasz = input("Szeretnél kártyát felhúzni, vagy megállsz? [húzás/megállás]:")
    print("\n\n\n\n\n\n\n")
    if valasz == "húzás":
        huz("jatekos")
        if jatekos > 21:
            megy = 0
        else:
            print(f"Dealer🐱‍👤: {dealer} \nJátékos😎: {jatekos}\n")
    elif valasz == "megállás":
        megy = 0

print("Üdvözöllek, ez itt egy BlackJack játék!")
print("A dealer és a játékos is húz kettő-kettő lapot. \n")
i = 2
while i > 0:
    huz("dealer")
    huz("jatekos")
    i = i-1

print(f"Dealer🐱‍👤: {dealer} \nJátékos😎: {jatekos}\n")
while megy == 1:
    dontes()
if megy == 0:
    print(f"Dealer🐱‍👤: {dealer} \nJátékos😎: {jatekos}\n")
    time.sleep(1)
    if jatekos <= 21:
        while dealer <= 16:
            huz("dealer")
            print("Húz a dealer...")
            time.sleep(1)
            print("\n\n\n\n\n\n\n")
            print(f"Dealer🐱‍👤: {dealer} \nJátékos😎: {jatekos}\n")
        if dealer > jatekos and dealer <= 21:
            print("❌Vesztettél!❌")
        else:
            print("💲Nyertél!💲")
    else:
        print("❌Vesztettél, mivel átlépted a 21-et!❌")