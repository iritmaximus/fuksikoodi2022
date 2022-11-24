tuotteet = []
kauppalista = []

def syota_resepti():
    pass

def syota_tuote():
    nimi = input("Syötä tuote: ")
    loytyy = False
    for tuote in tuotteet:
        if nimi == tuote.get("tuote"):
            loytyy = True
            kauppalista.append(tuote)
    if not loytyy:
        tuote = {}
        tuote["tuote"] = nimi
        yksikko = input("Mikä on tuotteen yksikkö? ")
        tuote["yksikko"] = yksikko
        osasto = input("Miltä osastolta tuote löytyy? ")
        tuote["osasto"] = osasto
        tuotteet.append(tuote)
        kauppalista.append(tuote)

while True:
    print("1: syötä yksittäinen tuote")
    print("2: syötä resepti")
    print("3: lopeta")
    toiminto = input("Valitse toiminto (1/2/3): ")
    if int(toiminto) == 1: # yksittäinen tuote
        syota_tuote()
    elif int(toiminto) == 2: # resepti
        syota_resepti()
    elif int(toiminto) == 3: # lopeta
        break
    else:
        print("Kokeile uudestaan")

print("kaikki tuotteet")
for tuote in tuotteet:
    print(tuote)

print("kauppalista")
for tuote in kauppalista:
    print(tuote)

        
