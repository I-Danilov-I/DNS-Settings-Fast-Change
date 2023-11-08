import socket  # Importiere das socket-Modul, um auf DNS-Informationen zuzugreifen

# Holen Sie die aktuelle DNS-Konfiguration für die Adresse "example.com" (oder eine beliebige andere Adresse)
dns_info = socket.getaddrinfo("example.com", None)

# Durchlaufe die Liste der DNS-Informationen
for info in dns_info:
    family, socktype, proto, canonname, sockaddr = info  # Entpacke die Informationen aus dem Tuple 'info'

    # DNS-Server-IP-Adressen abrufen
    dns_servers = socket.gethostbyname_ex(socket.gethostname())[2]
    print("DNS-Server-IP-Adressen:", dns_servers)

    # IPv4- und IPv6-Adressen abrufen
    ip_addresses = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if ':' not in ip]
    ipv6_addresses = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if ':' in ip]

    # Gebe die einzelnen DNS-Informationen aus
    print("IPv4-Adressen:", ip_addresses)
    print("IPv6-Adressen:", ipv6_addresses)
    print("Familie:", family)  # Zeige die Adressfamilie (z.B. AF_INET für IPv4)
    print("Sockentyp:", socktype)  # Zeige den Sockentyp (z.B. SOCK_STREAM für TCP)
    print("Protokoll:", proto)  # Zeige das Protokoll (z.B. IPPROTO_TCP für TCP)
    print("Kanonischer Name:", canonname)  # Zeige den kanonischen Namen (oder leeren String)
    print("Sockenadresse:", sockaddr)  # Zeige die Sockenadresse (z.B. IP-Adresse und Portnummer)
    print()  # Leerzeile für die Übersicht
