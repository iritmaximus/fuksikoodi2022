from tuotelista import read_csv
from kauppalista import kysy_kayttajalta

# from kauppalista import kysy_käyttäjältä


def main():
    valmiit_tuotteet = read_csv()

    kysy_kayttajalta()


if __name__ == "__main__":
    main()
