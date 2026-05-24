import pandas as pd
import smtplib
import datetime as dt
import random
my_email = "<EMAIL>"
my_password = "<PASSWORD>"
current_month = dt.datetime.now().month
current_day = dt.datetime.now().day
templates = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
birthday = pd.read_csv('birthdays.csv')
birthday_dict_list = birthday.to_dict(orient='records')
for i in range(len(birthday_dict_list)):
    day = birthday_dict_list[i]['day']
    month = birthday_dict_list[i]['month']
    if current_day == day and current_month == month:
        with open(f"letter_templates/{random.choice(templates)}", 'r') as file:
            file_content = file.read()
            file_content = file_content.replace('[NAME]', str(birthday_dict_list[i]['name']))
        connection = smtplib.SMTP('smtp.gmail.com', 587)
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_dict_list[i]['email'],msg=f"Subject: Happy Birthday!\n\n{file_content}".encode("utf-8"))
        connection.quit()




