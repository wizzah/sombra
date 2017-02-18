# Sombra scraper
The Sombra reveal is over, but this countdown (count up?) was fun.

## Install
- Create a virtual environment in python: `virtualenv venv` and activate it `source venv/bin/activate`
- install reqs with `pip install -r requirements.txt`
- Create settings.py based off of settings.py.template, use a slack webhook in SLACK_URL.
- Run `python get_sombra.py` for a quick check.
- if all is well, set up a cron job and let it go.
  - Don't be like me and spam your friends every 3 minutes by accident lololo
