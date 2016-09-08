from settings import SLACK_URL
import requests
import json
import re


def update_slack():
    if not SLACK_URL:
        print "No slack_url"
    else:
        # format sombra text?
        payload = {
            "channel": "#overwatch",
            "username": "Sombra",
            "text": sombra_text,
            "icon_emoji": ":skull:"
        }
        requests.post(SLACK_URL, data=json.dumps(payload))

sombra_text = None
try:
    result = requests.get('http://amomentincrime.com/')
    if result.status_code == 200:
        # cool
        result = re.split("%", result.text)
        result = re.split("... ", result[0])
        sombra_text = result[-1]+"%"
        update_slack()

    else:
        sombra_text = ":warning: ?que no respondio a 200? :warning:"

except:
    sombra_text = ":warning: yo quebre :/ :warning:"
