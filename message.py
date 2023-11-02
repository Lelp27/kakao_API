import requests
import json
from pathlib import Path
import argparse

def get_args():

    parser = argparse.ArgumentParser()
    parser.add_argument("-m", type=str,
                        default="End Command",
                        help="Message to send")
    parser.add_argument("-c", "--config", type=str,
                        default=Path.home() / Path(".kakao") / Path("config.json"),
                        help="config.json path")

    args = parser.parse_args()
    return args

def main():
    args = get_args()

    # Send Message with Access_TOKEN
    config_path = args.config
    with open(config_path) as f:
        config = json.load(f)

    REFRESH_URL = "https://kauth.kakao.com/oauth/token"
    REST_KEY = config["REST_KEY"]
    ACCESS_TOKEN = config["access_token"]

    message = args.m
    result = requests.post(verify=False,
        url="https://kapi.kakao.com/v2/api/talk/memo/default/send",
        headers={"Content-Type": "application/x-www-form-urlencoded",
                "Authorization": f"Bearer {ACCESS_TOKEN}"},
        data={
            "template_object": json.dumps({
                "object_type": "text",
                "text": f"{message}",
                "link": {
                    "web_url": "https://developers.kakao.com",
                    "mobile_web_url": "https://developers.kakao.com"
                },
                "button_title": "Done"
            })
        }
    )
    assert result.status_code == 200, "Message Error"
    print ("Done")

if __name__ == "__main__":
    main()
