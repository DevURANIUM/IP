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

        print(f"\033[92mIP: {ip_address}\033[0m")
        print(f"\033[94mStatus: \033[93m{status}\033[0m")
        print(f"\033[94mASN: \033[93m{asn}\033[0m")
        print(f"\033[94mProvider: \033[93m{provider}\033[0m")
        print(f"\033[94mOrganisation: \033[93m{organisation}\033[0m")
        print(f"\033[94mContinent: \033[93m{continent}\033[0m")
        print(f"\033[94mCountry: \033[93m{country}\033[0m")
        print(f"\033[94mISO code: \033[93m{isocode}\033[0m")
        print(f"\033[94mRegion: \033[93m{region}\033[0m")
        print(f"\033[94mRegion code: \033[93m{regioncode}\033[0m")
        print(f"\033[94mTimezone: \033[93m{timezone}\033[0m")
        print(f"\033[94mCity: \033[93m{city}\033[0m")
        print(f"\033[94mPostcode: \033[93m{postcode}\033[0m")
        print(f"\033[94mLatitude: \033[93m{latitude}\033[0m")
        print(f"\033[94mLongitude: \033[93m{longitude}\033[0m")
        print(f"\033[94mCurrency: \033[93m{currency}\033[0m")
        print(f"\033[94mCurrency symbol: \033[93m{symbol}\033[0m")
        print(f"\033[94mProxy: \033[93m{proxy}\033[0m")
        print(f"\033[94mIP type: \033[93m{IPtype}\033[0m")
        
    except Exception as e:
        print(f'\033[91mError: {str(e)}\033[0m')

def main():
    if len(sys.argv) < 2:
        print_banner()
        print_help()
        return

    if len(sys.argv) == 2 and not sys.argv[1].startswith('-'):
        address = sys.argv[1]
        ip_address = resolve_to_ip(address)
        if ip_address:
            check_ip_residential(ip_address)
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

