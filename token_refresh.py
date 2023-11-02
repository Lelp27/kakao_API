import requests
import json
from pathlib import Path

def main():
    config_path = Path.home() / Path(".kakao") / Path("config.json")
    with open(config_path) as f:
        config = json.load(f)

    REFRESH_URL = "https://kauth.kakao.com/oauth/token"
    REST_KEY = config["REST_KEY"]
    REFRESH_TOKEN = config["refresh_token"]

    response = requests.post(
        url=REFRESH_URL,
        headers={"Content-Type": "application/x-www-form-urlencoded;charset=utf-8"},
        data={
            "grant_type": "refresh_token",
            "client_id": f"{REST_KEY}",
            "refresh_token": f"{REFRESH_TOKEN}"
            },
        verify=False
        )
    assert response.status_code == 200, "Response Error"
    result = response.json()

    # Change token
    config["access_token"] = result["access_token"]
    if "refresh_token" in result.keys():
        config["refresh_token"] = result["refresh_token"]
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)
    print ("Done")

if __name__ == "__main__":
    main()
