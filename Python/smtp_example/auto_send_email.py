# -*- coding: utf-8 -*-
# @Time    : 10/3/2020 5:51 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: auto_send_email.py
# @Software: PyCharm

"""
Ref: https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp

I beleive I'm little late here. But I think this would help for the new peeps! If you're using smtp.gmail.com , then
you have to do the followwing: 1. Turn on the less secure apps 2. You'll get the security mail in your gmail inbox,
Click Yes,it's me in that. 3. Now run your code again.
"""

import smtplib, ssl
from email.mime.text import MIMEText
from email.header import Header
import pandas as pd
import calendar
from datetime import date
from credentials import cred

nth = {
    1: "1st",
    2: "2nd",
    3: "3rd",
    4: "4th",
    5: "5th"
    # etc
}

def send_mail(subject, text):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = cred.get("sender_email")
    receiver_email = cred.get("receiver_email")
    password = cred.get("password")

    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(text, 'plain', 'utf-8')
    message['From'] = Header("zdj@chinareformoverseas.com", 'utf-8')  # 发送者
    message['To'] = Header("zdj@chinareformoverseas.com", 'utf-8')  # 接收者

    subject = '重要：CDG工作提示！'
    message['Subject'] = Header(subject, 'utf-8')

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


def get_nth_week_of_month(today):
    week, day = divmod(today.day, 7)
    if day!=0:
        week += 1
    return week

def read_schedule():
    schedule = pd.read_excel("中后台财务岗_Time+Schedule.xlsx", index_col=0)
    current_week = get_current_week()
    current_week = "Feb.3rd w"
    return current_week, schedule.loc[current_week,:].dropna()

def get_current_week():
    today = date.today()
    week = get_nth_week_of_month(today)
    month_abbr = calendar.month_abbr[today.month]
    week_abbr = nth[week]
    return f"{month_abbr}.{week_abbr} w"

def check_already_sent(current_week):
    try:
        with open("already_sent.txt", "r") as f:
            for week in f.readlines():
                if current_week==week.replace("\n",""):
                    return True
    except FileNotFoundError:
        pass
    return False

def mark_already_sent(current_week):
    with open("already_sent.txt", "a") as f:
        f.write(f"{current_week}\n")

def auto_send_email():
    current_week, schedule = read_schedule()
    already_sent = check_already_sent(current_week)
    # print(f"Already sent: {already_sent}")
    if already_sent:
        print("Already sent.")
    elif schedule.empty:
        print("No task.")
    else:
        text = schedule.to_string().replace("\\n\\n", "") # .encode("utf-8").decode("utf-8")
        print(text)
        subject = "Reminder: CDG Todo List"
        send_mail(subject, text)
        mark_already_sent(current_week)

if __name__=="__main__":
    # send_mail("hello", "I am zdj.")
    auto_send_email()


