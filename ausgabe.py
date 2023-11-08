def ausgabe(text):
    print("\n")
    zeichen_anzahl = len(text)
    zeichen_anzahl = zeichen_anzahl + 44
    print(20*"_" + "[", text, "]" + 20 * "_")
    return zeichen_anzahl


def unterstrich(zeichen_anzahl):
    print(zeichen_anzahl * "_")
    print("\n")


def ausgabe_log(text):
    print("[" + text + "]")
