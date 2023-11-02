import requests
import json
from pathlib import Path
# Get Authorize CODE

config_path = Path.home() / Path(".kakao") / Path("config.json")

REST_KEY = input("Enter REST API key: ")
REDIRECT_URI = "http://localhost:5020"
OAUTH_URL = f"https://kauth.kakao.com/oauth/authorize?client_id={REST_KEY}&redirect_uri={REDIRECT_URI}&response_type=code&scope=talk_message"

session = requests.session()
response = session.get(OAUTH_URL, allow_redirects=False, verify=False)
assert response.status_code == 302, "Authrize Error"
print (f'Login with Kakao: {response.headers["Location"]}')
# response.url

# Paste Code from URL in BROWSER!
TOKEN_URI = "https://kauth.kakao.com/oauth/token"
AUTHORIZE_URL = input("Login with previous URL and Enter the Redirected URL here: ")
AUTHORIZE_CODE = AUTHORIZE_URL.split("=")[1]

# Get Authorize ToKEN
headers = {"Content-Type": "application/x-www-form-urlencoded;charset=utf-8"}
data = {
    "grant_type": 'authorization_code',
    "client_id": REST_KEY,
    "redirect_uri": REDIRECT_URI,
    "code":AUTHORIZE_CODE
    }
response = session.post(TOKEN_URI, headers=headers, data=data)
assert response.status_code == 200, "Recive Token Error"
ACCESS_TOKEN = response.json()["access_token"]
REFRESH_TOKEN = response.json()["refresh_token"]
config['refresh_token'] = REFRESH_TOKEN
config['access_token'] = ACCESS_TOKEN
config['REST_KEY'] = REST_KEY

with open(config_path, 'w') as f:
    json.dump(config, f, indent=4)

print (f"Done the access token: {ACCESS_TOKEN} is saved")
