# IP Information & Residential Check Tool

This script provides detailed information about an IP address by retrieving data from two sources:
1. [Check-host.net](https://check-host.net/) for general IP information.
2. [Proxycheck.io](https://proxycheck.io/) to determine if the IP address is residential and provide detailed data about the provider, ASN, and more.

## Features

- Fetches detailed information about an IP address, including ASN, provider, continent, country, region, city, and more.
- Provides residential check of the IP address, determining if it's a proxy or VPN.
- Easy-to-use command-line interface with two options:
   1. **IP Info**: Get general IP information.
   2. **IP Residential Check**: Check if the IP address is residential and gather additional details.

## Requirements

Before running the script, ensure you have the following installed:

- **Python 3.9+**
- Required Python packages:
  - `requests` (for sending HTTP requests)
  - `beautifulsoup4` (for parsing HTML responses)

### Installing the required Python packages

You can install the necessary Python packages by running:

```bash
pip install requests beautifulsoup4
```

## Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/noarche/IP
   cd IP
   ```

2. **Install the necessary dependencies**:
   Run the following command to install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

   Or install manually as mentioned in the **Requirements** section.

## How to Use

1. **Run the script**:
   Start the script by running:
   ```bash
   python3 ip.py 127.0.0.1
   ```

   The script will display detailed information about the IP address, including its location, ASN, provider, and whether it is a proxy or VPN.

## Code Overview

- **python ip.py -1 127.0.0.1**: Fetches general IP data from Check-host.net, including location, ASN, and ISP.
- **python ip.py 127.0.0.1**: Uses Proxycheck.io to determine if the IP is residential, including the provider, ASN, and other details like city, region, and timezone.

## Dependencies

- [Requests](https://docs.python-requests.org/en/latest/) - A simple HTTP library for Python.
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - A Python library for parsing HTML and XML documents.

To install the required packages, run:

```bash
pip install requests beautifulsoup4
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


# ꧁꧂  Buy me a coffee ☕

![qrCode](https://raw.githubusercontent.com/noarche/cd-ripper/main/unrelated-ignore/CryptoQRcodes.png)

**Bitcoin** address `bc1qnpjpacyl9sff6r4kfmn7c227ty9g50suhr0y9j`


**Ethereum** address `0x94FcBab18E4c0b2FAf5050c0c11E056893134266`


**Litecoin** address `ltc1qu7ze2hlnkh440k37nrm4nhpv2dre7fl8xu0egx`



-------------------------------------------------------------------

![noarche's GitHub stats](https://github-readme-stats.vercel.app/api?username=noarche&show_icons=true&theme=transparent)


## Credits

This script has been updated and customized to my personal preferance, a fork of the [original by devURANIUM](https://github.com/DevURANIUM/IP)

