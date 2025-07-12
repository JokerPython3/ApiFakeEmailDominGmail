# api create fake email domin @gmail.com
import requests

url = "https://gmailnator.p.rapidapi.com/generate-email"

payload = { "options": [2, 3] }
headers = {
	"x-rapidapi-key": "1de9396936msh17d3fd8046ecc10p190cf9jsnfb933e49af65",
	"x-rapidapi-host": "gmailnator.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
email = response.json()['email']

############################################################


# api get messages

import requests

url = "https://gmailnator.p.rapidapi.com/inbox"

payload = {
	"email": email,
	"limit": 10
}
headers = {
	"x-rapidapi-key": "1de9396936msh17d3fd8046ecc10p190cf9jsnfb933e49af65",
	"x-rapidapi-host": "gmailnator.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())

########################################################################


#join my channel
