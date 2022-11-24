"""
hoitaa tuotteiden kategorioiden lisäämistä
ja niiden puuttuessa, kysymistä

csv tiedosto, jossa on sanakirjoja
{
    tuote: tuotteen_nimi,
    osasto: tuotteen_osasto (esim hevi, leipä, etc)
}

"""


tiedostonimi = "tuotekategoriat.csv"


def onko_tuotekategoriaa(tuote: dict, tuotteet: list):
    """
    tarkistaa, onko tuotteen 'kategoria' tiedossa
    jos ei, niin lisää se listaan

    """
    for x in tuotteet:
        pass


def read_csv():
    """Palauttaa listan tuotteista, joista on jo tiedossa
    osasto"""
    tuotteet = []

    with open(tiedostonimi) as f:
        sisältö = f.read().splitlines()

    for line in sisältö:
        nimi, osasto = line.split(";")
        tuotteet.append({"nimi": nimi, "osasto": osasto})

    return tuotteet


if __name__ == "__main__":
    # onko_tuotekategoriaa()
    read_csv()
