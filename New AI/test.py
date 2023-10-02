# import google.generativeai as palm
# import os

# palm.configure(api_key=os.environ['AIzaSyAmMtufl_TPyWdLbuCFD5Lh8IEpJWrEXYo'])

# response = palm.generate_text(prompt="The opposite of hot is")
# print(response.result) #  'cold.'

# response = palm.chat(messages=["Hello."])
# print(response.last) #  'Hello! What can I help you with?'
# response.reply("Can you tell me a joke?")

# model = palm.get_model('models/chat-bison-001') 

# import pprint
# for model in palm.list_models():
#     pprint.pprint(model) 
