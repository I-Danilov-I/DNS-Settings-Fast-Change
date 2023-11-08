gesamt_breite = 130
text_lange = 0


def ausgabe(text):
    global text_lange
    text = str(text)
    text = text.upper()
    text_lange = len(text)
    zeichen_anzahl = (gesamt_breite - text_lange) / 2
    zeichen_anzahl = int(zeichen_anzahl)
    print("\n")
    print(zeichen_anzahl * "_" + "[ " + text + " ]" + zeichen_anzahl * "_")
    return zeichen_anzahl


def unterstrich(zeichen_anzahl):
    anzahl_zeichen_gesamt = zeichen_anzahl * 2 + text_lange + 4
    print(anzahl_zeichen_gesamt * "-")


def ausgabe_log(text):
    print("LOG:" + "[" + text + "]")
