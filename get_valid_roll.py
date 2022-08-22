import requests
import bs4


def validate(uname):
    url1 = (
        "http://portal.stjosephstechnology.ac.in/portal/forgotPassword?Username=%s"
        % uname
    )
    resp = requests.get(url1)
    bobby = resp.text
    if "Not" in bobby:
        return False
    else:
        return True
