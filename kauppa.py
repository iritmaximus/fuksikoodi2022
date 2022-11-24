def jarjesta_lista(tuotteet: list):
    kauppa = ["kuivatuotteet", "kylmätuotteet", "hevi", "pakasteet"]
    jarjastetty_lista = []
    for osasto in kauppa:
        for tuote in tuotteet:
            if tuote["osasto"] == osasto:
                jarjastetty_lista.append(tuote)
    return jarjastetty_lista

if __name__ == "__main__":
    x = jarjesta_lista(tuotteet, kauppa)
    print(x)