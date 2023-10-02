# Api Key
file = open("files\\api.txt", "r")
API = file.read()
file.close()

# Importing Openai
import Brain.openai as openai
from dotenv import load_dotenv

# Coding

openai.api_key = API
load_dotenv()
completion = openai.Completion()

def ReplyBrain(question,chat_log=None):
    FileLog = open("","r")
    chat_log_template = FileLog.read()
    FileLog.close()

    if chat_log == None:
        chat_log = chat_log_template
    prompt = f'{chat_log}You: {question}\nJarvis:'
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0,
        temperature=0.5
    )
    answer = response.choices[0].text.strip()
    chat_log_template_updated = chat_log_template + f"You: {question} \nJarvis: {answer}\n"
    FileLog = open("","w")
    FileLog.write(chat_log_template_updated)
    FileLog.close()
    return answer
