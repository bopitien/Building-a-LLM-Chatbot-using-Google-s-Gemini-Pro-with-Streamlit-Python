import requests

api_key = "AIzaSyCRtmjZPVXqou1LvyvVzkkeGlYwTkfsAWA"  
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
headers = {
    "Content-Type": "application/json"
}
data = {
    "contents": [{
        "parts": [{"text": "Explain how AI works"}]
    }]
}

response = requests.post(url + f"?key={api_key}", headers=headers, json=data)

if response.status_code == 200:
    print("Response from Gemini API:")
    print(response.json())
else:
    print(f"Error {response.status_code}: {response.json()}")
