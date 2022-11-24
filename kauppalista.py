tuotteet = []
kauppalista = []

def syota_resepti():
    pass

def onko_tuotteissa(tuote: dict): 
    """
    Tarkistaa löytyykö tuote tuotelistasta.
    """
    loytyyko = False
    for sanakirja in tuotteet:
        if tuote.get("tuote") == sanakirja.get("tuote"):
            loytyy = True
            break
    return loytyyko

def lisaa_uusi_tuote_tuotelistaan(tuote: dict): 
"""
Tarkistaa löytyykö tuottesta kaikki tarvittavat tiedot.
Jos tarvittava tieto puuttuu, kysyy käyttäjältä kyseisen tiedon.
Lisää tuotteen tuotelistaan.
"""
    tarvittavat_tiedot = ["nimi", "yksikkö", "osasto"]
    for tieto in tarvittavat_tiedot:
        if tuote.get(tieto, None) == None:
            tuote[tieto] = input(f"Mikä on tuotteen {tuote.get("nimi")} {tieto}? ")
    tuotteet.append(tuote)
        
def lisaa_kauppalistaan(tuote: dict)
    kauppalista.append(tuote)

def main():
    while True:
        print("Toiminnot:")
        print("1: syötä yksittäinen tuote")
        print("2: syötä resepti")
        print("3: lopeta")
        toiminto = input("Valitse toiminto (1/2/3): ")
        try:
            if int(toiminto) == 1: # yksittäinen tuote
                tuote = input("Syötä tuote: ")
                syota_tuote(tuote)
            elif int(toiminto) == 2: # resepti
                syota_resepti()
            elif int(toiminto) == 3: # lopeta
                break
        except:
            print("Kokeile uudestaan")

main()

        
