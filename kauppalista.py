from tuotelista import read_csv
from reseptit import luo_reseptit
from kauppa import jarjesta_lista

tuotteet = read_csv()
kauppalista = []
reseptit = luo_reseptit()

def onko_resepteissa(syote: str):
    for resepti in reseptit:
        if syote == resepti.get("nimi"):
            return resepti.get("ainekset")
    return False

def syota_resepti(resepti: str):
    uusi_resepti = {}
    uusi_resepti["nimi"] = resepti
    uusi_resepti["ainekset"] =[]

    ainekset = onko_resepteissa(resepti)

    if not ainekset:
        ainekset = []
        while True:
            tuote = input("Anna tuote: ")
            if tuote == " " or tuote == "":
                break
            ainekset.append(lisaa_uusi_tuote_tuotelistaan(tuote))
    uusi_resepti["ainekset"] = ainekset
    for aines in ainekset:
        kauppalista.append(aines)
    return uusi_resepti

def onko_tuotteissa(tuote: str): 
    """
    Tarkistaa löytyykö tuote tuotelistasta.
    """
    for sanakirja in tuotteet:
        if tuote == sanakirja.get("nimi"):
            return sanakirja.get("osasto")
    return False

def lisaa_uusi_tuote_tuotelistaan(tuote: str): 
    """
    Tarkistaa löytyykö tuottesta kaikki tarvittavat tiedot.
    Jos tarvittava tieto puuttuu, kysyy käyttäjältä kyseisen tiedon.
    Lisää tuotteen tuotelistaan.
    """
    uusi_tuote = {}
    uusi_tuote["nimi"] = tuote
    uusi_tuote["määrä"] = 0
    uusi_tuote["yksikkö"] = ""
    uusi_tuote["osasto"] = None

    

    osasto = onko_tuotteissa(uusi_tuote["nimi"])
    if not osasto:
        uusi_tuote["osasto"] = input(f"Miltä osastolta {tuote} löytyy? ")
        tuotteet.append({"nimi": tuote, "osasto": uusi_tuote["osasto"]})
    else:
        uusi_tuote["osasto"] = osasto
    uusi_tuote["määrä"] = input(f"Kuinka paljon tuotetta {tuote} tarvitaan? ")
    uusi_tuote["yksikkö"] = input(f"Mikä on tuotteen yksikkö? ")

   

    return uusi_tuote

def tulosta_kauppalista():
    print()
    print("Kauppalista:")
    print()
    for tuote in kauppalista:
        print(f'{tuote["nimi"]:<10} {tuote["määrä"]} x {tuote["yksikkö"]}')

def jarjesta_kauppalista():
    jarjestetty_kauppalista = {}
    for tuote in kauppalista:
        if tuote["osasto"] not in jarjestetty_kauppalista:
            jarjestetty_kauppalista[tuote["osasto"]] = [tuote]
        else:
            jarjestetty_kauppalista[tuote["osasto"]].append(tuote)
    return jarjestetty_kauppalista

def tulosta_jarjestetty_kauppalista(lista: dict):
    print()
    print("Järjestetty kauppalista:")
    print()
    print()
    for osasto, tuotteet in lista.items():
        print(osasto)
        print()
        for tuote in tuotteet:
            print(f'{tuote["nimi"]:<10} {tuote["määrä"]} x {tuote["yksikkö"]}')
        print()
        print()   




def kysy_kayttajalta():
    while True:
        print()
        print()
        print("Toiminnot:")
        print("1: syötä yksittäinen tuote")
        print("2: syötä resepti")
        print("3: lopeta")
        print("4: tulosta tuotteet")
        print("5. tulosta kauppalista")
        print("6: tulosta järjestetty kauppalista")
        toiminto = input("Valitse toiminto (1/2/3/4/5/6): ")
        if toiminto == "":
            continue
        if int(toiminto) == 1: # yksittäinen tuote
            tuote = input("Syötä tuote: ")
            uusi_tuote = lisaa_uusi_tuote_tuotelistaan(tuote)
            if tuote in kauppalista:
                kauppalista["tuote"] += uusi_tuote["määrä"]
            else:
                kauppalista.append(uusi_tuote)
        elif int(toiminto) == 2: # resepti
            resepti = input("Syötä resepti: ")
            ainekset = syota_resepti(resepti)
        elif int(toiminto) == 3: # lopeta
            break
        elif int(toiminto) == 4:
            print(tuotteet)
        elif int(toiminto) == 5:
            tulosta_kauppalista()
        elif int(toiminto) == 6:
            tulosta_jarjestetty_kauppalista(jarjesta_kauppalista())
        else:
            print("Kokeile uudestaan")

kysy_kayttajalta()

        
