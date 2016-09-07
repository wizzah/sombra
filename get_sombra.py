from selenium import webdriver
from settings import SLACK_URL
import requests
import json
import re

driver = webdriver.Firefox()
sombra_text = None
try:
    driver.get('http://amomentincrime.com/')
    result = driver.find_element_by_css_selector('body > p > font').text
    result = re.split("%", result)
    result = re.split("... ", result[0])
    sombra_text = result[-1]+"%"
    print sombra_text
except:
    sombra_text = "yo quebre :/"
    print sombra_text

driver.close()

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
