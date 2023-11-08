import wmi
import logging
import info_ausgabe


# Konfigurieren Sie das Logging
logging.basicConfig(filename='dns_settings.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s: %(message)s')


def change_dns_settings(primary_dns_ipv4, secondary_dns_ipv4):
    try:
        # Initialisieren Sie das WMI-Objekt
        logging.info("Initialisiere das WMI-Objekt")
        wmi_obj = wmi.WMI()

        # Ermitteln Sie die Netzwerkschnittstellen
        logging.info("Ermittle die Netzwerkschnittstellen")
        network_interfaces = wmi_obj.Win32_NetworkAdapterConfiguration()

        for interface in network_interfaces:
            # Überprüfen Sie, ob die Netzwerkschnittstelle IPv4-Unterstützung hat
            logging.info("Überprüfe IPv4-Unterstützung für die Schnittstelle %s", interface.Description)
            # Ändern Sie die IPv4-DNS-Server
            dns_servers = [server for server in [primary_dns_ipv4, secondary_dns_ipv4] if server]
            logging.info("Ändere die IPv4-DNS-Server auf %s für die Schnittelle %s", dns_servers, interface.Description)
            interface.SetDNSServerSearchOrder(DNSServerSearchOrder=dns_servers)

        logging.info("DNS-Einstellungen erfolgreich geändert.")
    except Exception as e:
        logging.error("Fehler beim Ändern der DNS-Einstellungen: %s", str(e))


# Konfigurieren Sie die gewünschten DNS-Server
primary_dns_ipv4 = "94.140.14.49"
secondary_dns_ipv4 = "94.140.14.59"

print(10 * "_", "Daten vorher:", 10 * "_")
info_ausgabe.print_network_settings()
print(50 * "-")

# Rufen Sie die Funktion zum Ändern der DNS-Einstellungen auf
logging.info("Rufe die Funktion zum Ändern der DNS-Einstellungen auf")
change_dns_settings(primary_dns_ipv4, secondary_dns_ipv4)

print(10 * "_", "Daten vorher:", 10 * "_")
info_ausgabe.print_network_settings()
print(50 * "-")