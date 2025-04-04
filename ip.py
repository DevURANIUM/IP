import sys
import requests
from bs4 import BeautifulSoup
import socket  

def print_banner():
    print(f"""
    \033[95m
    ██╗░░░██╗██████╗░░█████╗░███╗░░██╗██╗██╗░░░██╗███╗░░░███╗
    ██║░░░██║██╔══██╗██╔══██╗████╗░██║██║██║░░░██║████╗░████║
    ██║░░░██║██████╔╝███████║██╔██╗██║██║██║░░░██║██╔████╔██║
    ██║░░░██║██╔══██╗██╔══██║██║╚████║██║██║░░░██║██║╚██╔╝██║
    ╚██████╔╝██║░░██║██║░░██║██║░╚███║██║╚██████╔╝██║░╚═╝░██║
    ░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░╚═════╝░╚═╝░░░░░╚═╝\033[0m
          
          \033[91m            ų℘ɖąɬɛɖ ცყ אσα૨૮ɦε   \033[0m
    """)

def print_help():
    print(f"""
    \033[96mUsage:\033[0m
    \033[92m  python ip.py -1 <IP_OR_DOMAIN>\033[0m  : Get detailed IP information.
    \033[92m  python ip.py -2 <IP_OR_DOMAIN>\033[0m  : Check if the IP is residential.
    \033[92m  python ip.py <IP_OR_DOMAIN>\033[0m    : Default to checking if the IP is residential.
    \033[92m  python ip.py -h\033[0m                : Display this help message.
    """)

def resolve_to_ip(address):
    """Resolve a domain name to an IP address. If already an IP, return as is."""
    try:
        ip_address = socket.gethostbyname(address)
        return ip_address
    except socket.gaierror:
        print(f"\033[91mError: Unable to resolve domain '{address}' to an IP address.\033[0m")
        return None

def get_csrf_token():
    url = "https://check-host.net/ip-info"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    csrf_token_input = soup.find('input', {'name': 'csrf_token'})
    if csrf_token_input:
        csrf_token = csrf_token_input['value']
        return csrf_token
    else:
        print("\033[91mCSRF token not found.\033[0m")
        return None

def get_ip_info(ip_address):
    csrf_token = get_csrf_token()
    if csrf_token is not None:
        url = f"https://check-host.net/ip-info?host={ip_address}&csrf_token={csrf_token}"
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', class_='ipinfo-table')

        data = {}

        for row in table.find_all('tr'):
            columns = row.find_all('td')
            if len(columns) == 2:
                key = columns[0].get_text(strip=True)
                value = columns[1].get_text(strip=True)
                data[key] = value

        for key, value in data.items():
            print(f"\033[94m{key} : \033[93m{value}\033[0m")
    else:
        print("\033[91mCannot send request without CSRF token.\033[0m")

def get_ip_info_summary(ip_address):
    """Fetch and return a summary of IP info (Host name, IP range, Local time)."""
    csrf_token = get_csrf_token()
    if csrf_token is not None:
        url = f"https://check-host.net/ip-info?host={ip_address}&csrf_token={csrf_token}"
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', class_='ipinfo-table')

        data = {}

        for row in table.find_all('tr'):
            columns = row.find_all('td')
            if len(columns) == 2:
                key = columns[0].get_text(strip=True)
                value = columns[1].get_text(strip=True)
                data[key] = value

        host_name = data.get('Host name', 'N/A')
        ip_range = data.get('IP range', 'N/A')
        local_time = data.get('Local time', 'N/A')

        return {
            'Host name': host_name,
            'IP range': ip_range,
            'Local time': local_time
        }
    else:
        print("\033[91mCannot send request without CSRF token.\033[0m")
        return None

def check_ip_residential(ip_address):
    url = f'https://proxycheck.io/v2/{ip_address}?vpn=1&asn=1'
    response = requests.get(url)
    data = response.json()
    
    try:
        status = data.get('status', "")
        ip_data = data.get(ip_address, {})
        asn = ip_data.get('asn', "")
        provider = ip_data.get('provider', "")
        organisation = ip_data.get('organisation', "")
        continent = ip_data.get('continent', "")
        country = ip_data.get('country', "")
        isocode = ip_data.get('isocode', "")
        region = ip_data.get('region', "")
        regioncode = ip_data.get('regioncode', "")
        timezone = ip_data.get('timezone', "")
        city = ip_data.get('city', "")
        postcode = ip_data.get('postcode', "")
        latitude = ip_data.get('latitude', "")
        longitude = ip_data.get('longitude', "")
        currency = ip_data.get('currency', {}).get('code', "")
        symbol = ip_data.get('currency', {}).get('symbol', "")
        proxy = ip_data.get('proxy', "")
        IPtype = ip_data.get('type', "")

        return {
            "IP": ip_address,
            "Status": status,
            "ASN": asn,
            "Provider": provider,
            "Organisation": organisation,
            "Continent": continent,
            "Country": country,
            "ISO code": isocode,
            "Region": region,
            "Region code": regioncode,
            "Timezone": timezone,
            "City": city,
            "Postcode": postcode,
            "Latitude": latitude,
            "Longitude": longitude,
            "Currency": currency,
            "Currency symbol": symbol,
            "Proxy": proxy,
            "IP type": IPtype
        }
        
    except Exception as e:
        print(f'\033[91mError: {str(e)}\033[0m')
        return {}

def main():
    if len(sys.argv) < 2:
        print_banner()
        print_help()
        return

    if len(sys.argv) == 2 and not sys.argv[1].startswith('-'):
        address = sys.argv[1]
        ip_address = resolve_to_ip(address)
        if ip_address:
            print("\033[97m𝘗𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯•._.••`¯\033[0m")
            residential_results = []
            try:
                residential_results = check_ip_residential(ip_address)
            except Exception as e:
                print(f"\033[91mError during residential check: {str(e)}\033[0m")

            print("\033[96m𝘗𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯•._.••`¯´´•.¸¸.•`\033[0m")
            summary = {}
            try:
                summary = get_ip_info_summary(ip_address)
            except Exception as e:
                print(f"\033[91mError during IP info fetch: {str(e)}\033[0m")

            print("\n\033[92m𝘗𝘳𝘰𝘤𝘦𝘴𝘴𝘦𝘥•._.••`¯´´•.¸¸.•`´¯`••._.•\033[0m")
            if residential_results:
                for key, value in residential_results.items():
                    print(f"\033[94m{key}: \033[93m{value}\033[0m")
            if summary:
                print(f"\033[94mHost name: \033[93m{summary.get('Host name', 'N/A')}\033[0m")
                print(f"\033[94mIP range: \033[93m{summary.get('IP range', 'N/A')}\033[0m")
                print(f"\033[94mLocal time: \033[93m{summary.get('Local time', 'N/A')}\033[0m")
        return

    option = sys.argv[1]
    
    if option == '-h':
        print_help()
    elif option in ['-1', '-2']:
        if len(sys.argv) < 3:
            print("\033[91mError: IP address or domain is required.\033[0m")
            return
        
        address = sys.argv[2]
        ip_address = resolve_to_ip(address)
        if not ip_address:
            return

        if option == '-1':
            get_ip_info(ip_address)
        elif option == '-2':
            check_ip_residential(ip_address)
    else:
        print("\033[91mInvalid option.\033[0m")
        print_help()

if __name__ == "__main__":
    main()

