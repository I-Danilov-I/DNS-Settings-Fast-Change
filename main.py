import wmi
import logging

# Konfigurieren Sie das Logging
logging.basicConfig(filename='dns_settings.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s: %(message)s')


def change_dns_settings(dns_server_ipv4, dns_server_ipv6):
    try:
        # Initialisieren Sie das WMI-Objekt
        wmi_obj = wmi.WMI()

        # Ermitteln Sie die Netzwerkschnittstellen
        network_interfaces = wmi_obj.Win32_NetworkAdapterConfiguration()

        for interface in network_interfaces:
            # Überprüfen Sie, ob die Netzwerkschnittstelle IPv4-Unterstützung hat
            if interface.IPEnabled:
                # Ändern Sie die IPv4-DNS-Server
                if dns_server_ipv4:
                    logging.info("Ändere den IPv4-DNS-Server auf %s für die Schnittstelle %s", dns_server_ipv4, interface.Description)
                    interface.SetDNSServerSearchOrder(DNSServerSearchOrder=[dns_server_ipv4])

            # Überprüfen Sie, ob IPv6-Unterstützung für diese Schnittstelle verfügbar ist
            if hasattr(interface, "IPv6Enabled") and interface.IPv6Enabled:
                # Ändern Sie die IPv6-DNS-Server
                if dns_server_ipv6:
                    logging.info("Ändere den IPv6-DNS-Server auf %s für die Schnittelle %s", dns_server_ipv6, interface.Description)
                    interface.SetDNSServerSearchOrder(DNSServerSearchOrder=[dns_server_ipv6])

        logging.info("DNS-Einstellungen erfolgreich geändert.")
    except Exception as e:
        logging.error("Fehler beim Ändern der DNS-Einstellungen: %s", str(e))


# Konfigurieren Sie die gewünschten DNS-Server
dns_server_ipv4 = "8.8.8.8"
dns_server_ipv6 = "2001:4860:4860::8888"

# Rufen Sie die Funktion zum Ändern der DNS-Einstellungen auf
change_dns_settings(dns_server_ipv4, dns_server_ipv6)
