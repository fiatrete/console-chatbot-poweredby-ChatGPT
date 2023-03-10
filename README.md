# console-chatbot-poweredby-ChatGPT
A simple console chatbot implemented with Python and official OpenAI API using model `gpt-3.5-turbo`. ChatGPT is powered by `gpt-3.5-turbo`, OpenAI’s most advanced language model.

You can consider it as the code way of using ChatGPT, and demo for OpenAI API.

It's much fun to find that:

1. Using the API to access ChatGPT is **much faster** than directly using the web version of ChatGPT.
2. Replies from ChatGPT are **delivered all at once**(code version), rather than one character at a time(web version).
3. Simple is good, I have shifted most of my conversations with ChatGPT to this small bot.

## How to use
1.clone code from github 

```bash
git clone git@github.com:fiatrete/console-chatbot-poweredby-ChatGPT.git
cd console-chatbot-poweredby-ChatGPT
```

2.setup and activate venv

```bash
python3 -m venv .
source bin/activate
```

3.install openai lib

```bash
pip install openai
```	

4.get your API Keys from `https://platform.openai.com/account/api-keys`, and set `openai.api_key` in code.

![sec-keys](images/sec-keys.png)

5.run and have fun

![chat](images/chat.png)
