
import os
import openai
import logging as log

log.basicConfig(filename='openai-history.log', encoding='utf-8', level=log.DEBUG)

# Load your API key from an environment variable or secret management service
openai.api_key = "Paste your KEY here."

messages=[
    {"role": "system", "content": "You are a helpful assistant."},
]

while True:
    user_input = input("Q: ")
    if user_input == 'q':
        break
    
    log.info('Q:'+user_input)
    item =  {"role": "user", "content": user_input}
    messages.append(item)

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )
    log.info(response)
    print('A: '+str(response['choices'][0]['message']['content'])+'\n')
    messages.append(response['choices'][0]['message'])