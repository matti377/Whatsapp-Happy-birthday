##from whatsapp_api_client_python import API
import random
import pandas as pd
from datetime import datetime
import os
import openai

#Import secret variables
from config import OPENAI_API_KEY, TEXTMESSAGE_OPENAI_PROMPT_Part1, TEXTMESSAGE_OPENAI_PROMPT_Part2, GENERATE_AI_TEXT, TABEL_NAME

#get current date
current_date = datetime.now().date()

#get data from exel sheet
data = pd.read_excel(TABEL_NAME)

row_numbers = data.index[data['Birth Date'].dt.date == current_date].tolist()

column_values = data.iloc[:, 1]

for value in column_values:
    print(value)

NAME = value

#OGenerate AI Message
openai.api_key = OPENAI_API_KEY
CHATGPT_TEXT = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages = [{"role": "user", "content" : TEXTMESSAGE_OPENAI_PROMPT_Part1 + NAME + TEXTMESSAGE_OPENAI_PROMPT_Part2}]
)


#generate random message from list
number = random.randint(1, 9)
print(number)
if number == 1:
    RANDOMTEXT = "Happy Birthday " + NAME
elif number == 2:
    RANDOMTEXT = "Vill Gléck fir dain Gebuertsdaag"
elif number == 3:
    RANDOMTEXT = "Happy Birthday :)"
elif number == 4:
    RANDOMTEXT = "Happy Birthday " + NAME + "🎂"
elif number == 5:
    RANDOMTEXT = "Happy Birthday 🎉🎂"
elif number == 6:
    RANDOMTEXT = "Happy Birthday 🥳🎁🎈"
elif number == 7:
    RANDOMTEXT = "Happy Birthday 🎂🎁" 
elif number == 8:
    RANDOMTEXT = "Happy Birthday 🍰🎂🎈"
elif number == 9:
    RANDOMTEXT = "Happy Birthday"


#Generate final message
if GENERATE_AI_TEXT == 1:
    FINALTEXT = CHATGPT_TEXT
elif GENERATE_AI_TEXT == 2:
    FINALTEXT = RANDOMTEXT



greenAPI = API.GreenApi(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)


def main():
    response = greenAPI.sending.sendMessage("TEL_NUMBER@c.us", FINALTEXT)

    print(response.data)


if __name__ == '__main__':
    main()