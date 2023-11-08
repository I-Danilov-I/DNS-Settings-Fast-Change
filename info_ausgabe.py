import socket


def ip_info():
    # DNS-Server-IP-Adressen abrufen
    dns_servers = socket.gethostbyname_ex(socket.gethostname())[2]

    # IPv4- und IPv6-Adressen abrufen
    ip_addresses = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]]
    ip_addresses_ipv4 = [ip for ip in ip_addresses if ':' not in ip]
    ip_addresses_ipv6 = [ip for ip in ip_addresses if ':' in ip]

    print("DNS-Server-IP-Adressen:", dns_servers)
    print("IPv4-Adressen:", ip_addresses_ipv4)

    if ip_addresses_ipv6:
        print("IPv6-Adressen:", ip_addresses_ipv6)
    else:
        print("Keine IPv6-Adressen konfiguriert.")

    if len(dns_servers) > 1:
        print("Zusätzliche DNS-Server konfiguriert.")
    else:
        print("Keine zusätzlichen DNS-Server konfiguriert.")
