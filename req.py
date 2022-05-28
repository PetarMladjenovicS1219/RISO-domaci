import requests,json
url = 'http://localhost:8081/users'
payload = json.dumps({
            "ime":"test",
            "prezime": "test",
            "smer": "it",
            "username" : "test",
            "predmeti": [
                {
                    "ime": "test",
                    "espb":2,
                }
            ]
            })
headers = {'Content-Type': 'application/json'}

req = requests.request("POST",url,headers=headers,data=payload)
print(req.text)
