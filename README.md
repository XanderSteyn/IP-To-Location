---

# 🌍 IP Information Lookup

A simple Python tool that retrieves detailed information about a given IP address using the [ipinfo.io](https://ipinfo.io/) API.

⚠️ **Use responsibly** – This tool is designed for educational and personal use only.

## ⚙️ Features
- Retrieves detailed information about an IP address, including hostname, city, region, country, organization, and more.
- Uses the `requests` library to interact with the ipinfo.io API.
- Outputs the retrieved details in a clean format.

## 🚀 Installation

### Prerequisites

To run this project, you need Python 3.x installed and the `requests` library.

Install the required package:

```bash
pip install requests
```

### 🛠️ Setup

1. Clone the repository to your local machine :

   ```bash
   git clone https://github.com/XanderSteyn/IP-To-Location.git
   cd IP-To-Location
   ```

2. Run the script:

   ```bash
   python IPLookup.py
   ```

### 📦 Dependencies

- `requests` A simple HTTP library to interact with the ipinfo.io API.

## 🛑 How It Works

1. The script prompts you to input an IP address.
2. It sends a GET request to the ipinfo.io API to fetch the details of the provided IP.
3. The retrieved information is then displayed, including the IP, hostname, city, region, country, location coordinates, organization, postal code, timezone, and anycast information.

## 📝 Usage

1. Run the script :
   ```bash
   python IPLookup.py
   ```

2. Enter the IP address when prompted :
   ```text
   IP: 8.8.8.8
   ```

3. The script will then display the details for the provided IP.

## ⚙️ Configuration

- **API Source** : The script uses the [ipinfo.io](https://ipinfo.io/) API, which provides various details about the given IP address.
- **Error Handling** : If a requested field is not available, it will display 'N/A'.

---
