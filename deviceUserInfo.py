import requests
from requests.auth import HTTPBasicAuth

USER = "devnetuser"
PASS = "Cisco123!"
URL = "https://sandboxdnac.cisco.com/api/system/v1/auth/token"

headers = {'Content-Type': 'application/json'}

response = requests.post(URL, auth=HTTPBasicAuth(USER, PASS), headers=headers, verify=False)

token = response.json()['Token']

URL2 = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"

getHeader = {'Accept': 'application/json', 'X-auth-token': token}


getResponse = requests.get(URL2, headers=getHeader, verify=False)

devicesJSON = getResponse.json()

devices = getResponse.json()['response']

for soda in devices:
	coke = soda['hostname']
	pepsi = soda['macAddress']
	drpib = soda['family']
	print("The Device Named: " + str(coke) + " has the mac address of: " + str(pepsi) + " and belongs to the family: " + str(drpib))
