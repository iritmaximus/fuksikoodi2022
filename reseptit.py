reseptit = []

nakkimunakas = {
    "nimi": "nakkimunakas",
    "ainekset": [
        {"nimi": "nakki", "määrä": 6, "yksikkö": "kpl", "osasto": "kylmätuotteet"},
        {"nimi": "muna", "määrä": 2, "yksikkö": "kpl", "osasto": "kylmätuotteet"},
    ],
}
reseptit.append(nakkimunakas)

smoothie = {
    "nimi": "smoothie",
    "ainekset": [{"omena": 2, "banaani": 2, "appelsiini": 1}],
}
reseptit.append(smoothie)

riisipuuro = {"nimi": "riisipuuro", "ainekset": [{"maito": 1, "riisi": 1}]}
reseptit.append(riisipuuro)

looppi = True

kauppalista = []


while looppi is True:
    resepti = input("Anna resepti: ")
    for x in reseptit:
        if x["nimi"] == resepti:
            print("Hienoa, resepti löytyi!")
            for y in x["ainekset"]:
                kauppalista.append(y)
            looppi = False
            break
    else:
        print("Valitettavasti reseptiä ei löytynyt")
        print("Maistuisiko smoothie?")


print(kauppalista)
