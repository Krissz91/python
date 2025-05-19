#!/usr/bin/python3

import whois

def get_domain_info(domain_name):
    try:
        domain = whois.whois(domain_name)

        creation_date = domain.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        expiration_date = domain.expiration_date
        if isinstance(expiration_date, list):
            expiration_date = expiration_date[0]

        print(f"Domain Name: {domain.domain_name or 'N/A'}")
        print(f"Registrar: {domain.registrar or 'N/A'}")
        print(f"Creation Date: {creation_date or 'N/A'}")
        print(f"Expiration Date: {expiration_date or 'N/A'}")
        print(f"Name Servers: {', '.join(domain.name_servers) if domain.name_servers else 'N/A'}")

    except Exception as e:
        print(f"Error fetching information: {e}")

if __name__ == "__main__":
    domain = input("Enter a domain name (e.g., example.com): ")
    get_domain_info(domain)

# sudo apt update
# sudo apt/yum/dnf install python3 python3-pip -y
# sudo pip3 install python-whois or sudo pip3 install python-whois --break-system-packages
