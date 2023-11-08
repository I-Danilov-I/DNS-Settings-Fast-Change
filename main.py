import ausgabe
import ipv4_change
import einstellungen_anzeigen


# Konfigurieren Sie die gewünschten DNS-Server
primary_dns_ipv4 = "94.140.14.49"
secondary_dns_ipv4 = "94.140.14.59"

# Log einträge leeren
with open("dns_settings.log", "r+") as f:
    f.truncate(0)


zeichenanzahl = ausgabe.ausgabe("Aktuelle Einstellungen")
einstellungen_anzeigen.print_network_settings()
ausgabe.unterstrich(zeichenanzahl)


ipv4_change.change_dns_settings(primary_dns_ipv4, secondary_dns_ipv4)

zeichenanzahl = ausgabe.ausgabe("Aktuelle Einstellungen")
einstellungen_anzeigen.print_network_settings()
ausgabe.unterstrich(zeichenanzahl)
