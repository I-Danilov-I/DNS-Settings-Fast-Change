import wmi


def print_network_settings():
    c = wmi.WMI()
    network_configs = c.Win32_NetworkAdapterConfiguration(IPEnabled=True)

    for config in network_configs:
        print("Adapter: {}".format(config.Description))
        print("IPv4-Adresse(n): {}".format(", ".join(config.IPAddress)))
        print("IPv4-Subnetzmaske(n): {}".format(", ".join(config.IPSubnet)))
        print("IPv4-Gateway(s): {}".format(", ".join(config.DefaultIPGateway)))

        # Abrufen der DNS-Server-Informationen für IPv4
        dns_ipv4 = [dns for dns in config.DNSServerSearchOrder if ':' not in dns]
        print("DNS-Server IPv4: {}".format(", ".join(dns_ipv4)))

        # Abrufen der DNS-Server-Informationen für IPv6
        dns_ipv6 = [dns for dns in config.DNSServerSearchOrder if ':' in dns]
        print("DNS-Server IPv6: {}".format(", ".join(dns_ipv6)))

        print()


if __name__ == "__main__":
    print_network_settings()
