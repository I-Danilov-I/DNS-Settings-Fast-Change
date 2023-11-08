import sys

import ausgabe
import ipv4_change
import einstellungen_anzeigen

try:
    # Konfigurieren Sie die gewünschten DNS-Server
    primary_dns_ipv4 = "94.140.14.49"
    secondary_dns_ipv4 = "94.140.14.59"

    # Log einträge leeren
    with open("dns_settings.log", "r+") as f:
        f.truncate(0)

    zeichenanzahl = ausgabe.ausgabe("Aktuelle Einstellungen")
    einstellungen_anzeigen.print_network_settings()
    ausgabe.unterstrich(zeichenanzahl)

    zeichenanzahl = ausgabe.ausgabe("Diese Einstellungen werden geändert")
    print("DNS-Server IPv4 Primär: ", primary_dns_ipv4)
    print("DNS-Server IPv4 Alternative: ", secondary_dns_ipv4)
    ausgabe.unterstrich(zeichenanzahl)
    input("Drücken sie Enter um die Einstellungen auf folgende daten zu setzen:")
    print("\n")

    ipv4_change.change_dns_settings(primary_dns_ipv4, secondary_dns_ipv4)

    zeichenanzahl = ausgabe.ausgabe("Einstellungen nach der Änderung")
    einstellungen_anzeigen.print_network_settings()
    ausgabe.unterstrich(zeichenanzahl)
    input("Zum beenden [Enter] drücken:")


except KeyboardInterrupt:
    print("\n")
    sys.exit("Beendet durch Benutzer.")
