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
   git clone https://github.com/DevURANIUM/IP.git
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
   python3 ip.py
   ```

2. **Choose an option**:
   - **Option 1**: Enter `1` to retrieve general IP information from [Check-host.net](https://check-host.net/).
   - **Option 2**: Enter `2` to check if the IP is residential using [Proxycheck.io](https://proxycheck.io/).

### Example

1. Run the script:

   ```bash
   python3 ip.py
   ```

2. Enter the IP address when prompted, and choose between:
   - **Option 1**: General IP Info (Check-host.net)
   - **Option 2**: Residential Check (Proxycheck.io)

   The script will display detailed information about the IP address, including its location, ASN, provider, and whether it is a proxy or VPN.

## Code Overview

- **Banner Printing**: Displays a custom banner when the script starts.
- **IP Information Retrieval**: Fetches general IP data from Check-host.net, including location, ASN, and ISP.
- **Residential Check**: Uses Proxycheck.io to determine if the IP is residential, including the provider, ASN, and other details like city, region, and timezone.
- **CSRF Token Handling**: Automatically retrieves and handles CSRF tokens required for making requests to Check-host.net.

## Dependencies

- [Requests](https://docs.python-requests.org/en/latest/) - A simple HTTP library for Python.
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - A Python library for parsing HTML and XML documents.

To install the required packages, run:

```bash
pip install requests beautifulsoup4
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support & Contributions

If you encounter any issues or have suggestions for improvement, please reach out via:

- [Telegram](https://t.me/DevURANIUM)
- [GitHub Issues](https://github.com/DevURANIUM/IP/issues)

## Donation Links

Support the project through donations:

- **BTC**: `bc1qcclcp574hnznm0nmdzzf0ta7366svjskttqks3`
- **TRON**: `TXJqhhwvkrTdnf5HReZf55hEzZuxjto3R4`
- **USDT-(TRC20)**: `TXJqhhwvkrTdnf5HReZf55hEzZuxjto3R4`
- **TON**: `UQAJH2N0pqpvC9YN841w5NH1dCN9Lakwkpjvoy7vXf-vfqgv`

---

This file provides an organized and professional overview of the project, similar to the format you requested.
