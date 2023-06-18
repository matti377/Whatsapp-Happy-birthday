#import requirements
import random
import pandas as pd
from datetime import datetime
import os
import openai

#Import secret variables
from config import OPENAI_API_KEY, TEXTMESSAGE_OPENAI_PROMPT_Part1, TEXTMESSAGE_OPENAI_PROMPT_Part2, GENERATE_AI_TEXT, TABEL_NAME, RANDOMTEXT1, RANDOMTEXT2, RANDOMTEXT3, RANDOMTEXT4, RANDOMTEXT5, RANDOMTEXT6, RANDOMTEXT7, RANDOMTEXT8, PREDEFINED_MESSAGE

#get current date
current_date = datetime.now().date()

#get data from exel sheet
data = pd.read_excel(TABEL_NAME)

row_numbers = data.index[data['Birth Date'].dt.date == current_date].tolist()

column_values = data.iloc[:, 1]

for value in column_values:
    print(value)

NAME = value

column_values = data.iloc[:, 3]

for value2 in column_values:
    print(value2)

TEL_NUMBER = value2

#Generate AI Message
if GENERATE_AI_TEXT == 1:
    openai.api_key = OPENAI_API_KEY
    CHATGPT_TEXT = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages = [{"role": "user", "content" : TEXTMESSAGE_OPENAI_PROMPT_Part1 + NAME + TEXTMESSAGE_OPENAI_PROMPT_Part2}]
    )


#generate random message from list
elif GENERATE_AI_TEXT == 2:
    number = random.randint(1, 8)
    print(number)
    if number == 1:
        RANDOMTEXT = RANDOMTEXT1
    elif number == 2:
        RANDOMTEXT = RANDOMTEXT2
    elif number == 3:
        RANDOMTEXT = RANDOMTEXT3
    elif number == 4:
        RANDOMTEXT = RANDOMTEXT4
    elif number == 5:
        RANDOMTEXT = RANDOMTEXT5
    elif number == 6:
        RANDOMTEXT = RANDOMTEXT6
    elif number == 7:
        RANDOMTEXT = RANDOMTEXT7
    elif number == 8:
        RANDOMTEXT = RANDOMTEXT8



#Generate final message
if GENERATE_AI_TEXT == 0:
    FINALTEXT = PREDEFINED_MESSAGE
elif GENERATE_AI_TEXT == 1:
    FINALTEXT = CHATGPT_TEXT
elif GENERATE_AI_TEXT == 2:
    FINALTEXT = RANDOMTEXT



# For sending a Text messages
#sending still in programmation
print(current_date)
print(FINALTEXT)
print(TEL_NUMBER)