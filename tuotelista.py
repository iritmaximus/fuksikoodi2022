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


def onko_tuotekategoriaa(tuote: dict, valmiit_tuotteet: list):
    """
    tarkistaa, onko tuotteen 'kategoria' tiedossa
    jos ei, niin lisää se listaan

    """
    return False if tuote.osasto is None else True


def read_csv():
    """Palauttaa listan tuotteista, joista on jo tiedossa
    osasto"""
    tuotteet = []

    with open(tiedostonimi) as f:
        sisältö = f.read().splitlines()

    for line in sisältö:
        nimi, osasto = line.split(";")
        tuotteet.append({"nimi": nimi, "osasto": osasto})

    # print(tuotteet)

    return tuotteet


if __name__ == "__main__":
    # onko_tuotekategoriaa()
    read_csv()
