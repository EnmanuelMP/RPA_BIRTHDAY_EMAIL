import smtplib
import datetime as dt
import pandas as pd
import random
import sys

MY_EMAIL =""
PASSWORD_TOKEN = ""


def main():
    # STEP 1: GET CURRENT DAY AND MONTH
    today:tuple = (dt.datetime.now().month, dt.datetime.now().day)


    # STEP 2: GET BIRTHDAY DATA AND ADD IT TO A LIST
    df: pd.DataFrame = pd.read_csv('birthdays.csv')
    birthdays:dict = {(row["month"], row["day"]): row for (index, row) in df.iterrows()}

    # STEP 3: CHECK IF THERE IS ANY BIRTHDAY SCHEDULED FOR TODAY. IF NOT, EXIT THE PROGRAM
    if today not in birthdays:
        print("No birthdays are scheduled for today. Exiting the program.")
        sys.exit()

    # STEP 4: GET PERSON'S BIRTHDAY AND A RANDOM LETTER PATH
    birthday_person = birthdays[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

    # STEP 5: OPEN THE LETTER FILE AND REPLACE ITS VARIABLES
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("*|NAME|*", birthday_person["name"])

    # STEP 6: SEND THE EMAIL
    with smtplib.SMTP("smtp.gmail.com") as connection: # you can change email provider
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD_TOKEN)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=birthday_person["email"],msg=f"Subject: Happy Birthday!\n\n{contents}")