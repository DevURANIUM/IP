
# ###############################

# import requests
# from bs4 import BeautifulSoup

# print(f"""
# \033[34m
# ██╗░░░██╗██████╗░░█████╗░███╗░░██╗██╗██╗░░░██╗███╗░░░███╗
# ██║░░░██║██╔══██╗██╔══██╗████╗░██║██║██║░░░██║████╗░████║
# ██║░░░██║██████╔╝███████║██╔██╗██║██║██║░░░██║██╔████╔██║
# ██║░░░██║██╔══██╗██╔══██║██║╚████║██║██║░░░██║██║╚██╔╝██║
# ╚██████╔╝██║░░██║██║░░██║██║░╚███║██║╚██████╔╝██║░╚═╝░██║
# ░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░╚═════╝░╚═╝░░░░░╚═╝
      
#       Dev : DevUranium.t.me
#       GitHUB : 
#       """)

# def get_csrf_token():
#     url = "https://check-host.net/ip-info"
#     response = requests.get(url)
#     response.raise_for_status()
#     soup = BeautifulSoup(response.text, 'html.parser')

#     csrf_token_input = soup.find('input', {'name': 'csrf_token'})
#     if csrf_token_input:
#         csrf_token = csrf_token_input['value']
#         return csrf_token
#     else:
#         print("CSRF token not found.")
#         return None

# def send_request(ip_address):
#     csrf_token = get_csrf_token()
#     if csrf_token is not None:
#         url = f"https://check-host.net/ip-info?host={ip_address}&csrf_token={csrf_token}"
#         response = requests.get(url)
#         response.raise_for_status()

#         soup = BeautifulSoup(response.text, 'html.parser')
#         table = soup.find('table', class_='ipinfo-table')

#         data = {}

#         for row in table.find_all('tr'):
#             columns = row.find_all('td')
#             if len(columns) == 2:
#                 key = columns[0].get_text(strip=True)
#                 value = columns[1].get_text(strip=True)
#                 data[key] = value

#         for key, value in data.items():
#             print(f"{key} : {value}")
#     else:
#         print("Cannot send request without CSRF token.")

# ip = input("\033[32mIP Enter : \033[0m")

# send_request(ip)

# ###############################


import requests
from bs4 import BeautifulSoup

def print_banner():
    print(f"""
    \033[34m
    ██╗░░░██╗██████╗░░█████╗░███╗░░██╗██╗██╗░░░██╗███╗░░░███╗
    ██║░░░██║██╔══██╗██╔══██╗████╗░██║██║██║░░░██║████╗░████║
    ██║░░░██║██████╔╝███████║██╔██╗██║██║██║░░░██║██╔████╔██║
    ██║░░░██║██╔══██╗██╔══██║██║╚████║██║██║░░░██║██║╚██╔╝██║
    ╚██████╔╝██║░░██║██║░░██║██║░╚███║██║╚██████╔╝██║░╚═╝░██║
    ░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░╚═════╝░╚═╝░░░░░╚═╝\033[0m
    """)

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
        print("CSRF token not found.")
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
            print(f"\033[36m{key} : \033[33m{value}")
    else:
        print("Cannot send request without CSRF token.")

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

        print(f"IP: {ip_address}")
        print(f"Status: {status}")
        print(f"ASN: {asn}")
        print(f"Provider: {provider}")
        print(f"Organisation: {organisation}")
        print(f"Continent: {continent}")
        print(f"Country: {country}")
        print(f"ISO code: {isocode}")
        print(f"Region: {region}")
        print(f"Region code: {regioncode}")
        print(f"Timezone: {timezone}")
        print(f"City: {city}")
        print(f"Postcode: {postcode}")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
        print(f"Currency: {currency}")
        print(f"Currency symbol: {symbol}")
        print(f"Proxy: {proxy}")
        print(f"IP type: {IPtype}")
        
    except Exception as e:
        print(f'Error: {str(e)}')

def main():
    print_banner()
    print("Choose an option:")
    print("1. IP Info")
    print("2. IP Check Residential")
    
    choice = input("Enter number: ")
    
    if choice not in ['1', '2']:
        print("\033[31mInvalid choice.\033[0m")
        return

    ip = input("Enter IP address: ")
    
    if choice == '1':
        get_ip_info(ip)
    elif choice == '2':
        check_ip_residential(ip)

if __name__ == "__main__":
    main()

