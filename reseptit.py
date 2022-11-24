reseptit = []

nakkimunakas = {
    "nimi": "nakkimunakas",
    "ainekset": [
        {"nimi": "nakki", "määrä": 1, "yksikkö": "500 g paketti", "osasto": "kylmätuotteet"},
        {"nimi": "muna", "määrä": 1, "yksikkö": "6 kpl paketti", "osasto": "kylmätuotteet"},
    ]
}
reseptit.append(nakkimunakas)

smoothie = {
    "nimi": "smoothie",
    "ainekset": [{"nimi": "omena", "määrä": 2, "yksikkö": "kpl", "osasto": "heviosasto"}, 
    {"nimi": "banaani", "määrä": 2, "yksikkö": "kpl", "osasto": "heviosasto"},
    {"nimi": "appelsiini", "määrä": 1, "yksikkö": "kpl", "osasto": "heviosasto"}]}

reseptit.append(smoothie)

riisipuuro = {"nimi": "riisipuuro", "ainekset": [{"nimi": "riisi", "määrä": 1, "yksikkö": "500 g paketti", "osasto": "kuivaosasto"}, 
    {"nimi": "maito", "määrä": 1, "yksikkö": "litra", "osasto": "kylmäosasto"}]}

reseptit.append(riisipuuro)

print(reseptit)
