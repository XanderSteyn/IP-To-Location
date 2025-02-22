import requests
import os

def GetDetails(IP):
    URL = f"https://ipinfo.io/{IP}/json"
    Response = requests.get(URL)
    Response.raise_for_status()
    return Response.json()

IP = input("IP: ")
Details = GetDetails(IP)

os.system("cls")

print(f"IP Address       {Details.get('ip', 'N/A')}")
print(f"Hostname         {Details.get('hostname', 'N/A')}")
print(f"City             {Details.get('city', 'N/A')}")
print(f"Region           {Details.get('region', 'N/A')}")
print(f"Country          {Details.get('country', 'N/A')}")
print(f"Location         {Details.get('loc', 'N/A')}")
print(f"Organization     {Details.get('org', 'N/A')}")
print(f"Postal Code      {Details.get('postal', 'N/A')}")
print(f"Timezone         {Details.get('timezone', 'N/A')}")
print(f"Anycast          {Details.get('anycast', 'N/A')}")