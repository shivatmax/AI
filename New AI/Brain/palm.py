import requests
import json

def ReplyBrain(question,chat_log=None):
    FileLog = open("Database\chat_log.txt","r")
    chat_log_template = FileLog.read()
    FileLog.close()

    if chat_log == None:
        chat_log = chat_log_template
    prompt = f'{chat_log}You: {question}\nJarvis:'
    url = 'https://generativelanguage.googleapis.com/v1beta2/models/text-bison-001:generateText?key=AIzaSyAmMtufl_TPyWdLbuCFD5Lh8IEpJWrEXYo'
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
    "prompt": {
        "text": prompt
    }
}
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        answer = response.json()['candidates'][0]['output']
        chat_log_template_updated = chat_log_template + f"You: {question} \nJarvis: {answer}\n"
        FileLog = open("Database\chat_log.txt","w")
        FileLog.write(chat_log_template_updated)
        FileLog.close()
        return answer
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
        return None

