import smtplib
import datetime as dt
import random


def send_email():
    quotes = [str(i) for i in open('quotes.txt', 'r')]
    quoteSend = random.choice(quotes)
    my_email = "testingcde44@gmail.com"
    password = "############"

    connection = smtplib.SMTP("smtp.gmail.com")
    # this makes our connection secure
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="testingcde44@yahoo.com",
        msg=f"Subject:Wednesday Weekly Quotes!\n\n{quoteSend}")
    connection.close()


now = dt.datetime.now()
if now.weekday() == 2:
    send_email()




