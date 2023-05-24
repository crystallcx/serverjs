import requests
import json
import colorama

SERVER_IP = "10.0.0.18"
URL = "http://" + SERVER_IP + "/generate"

USERTOKEN = "<|prompter|>"
ENDTOKEN = "<|endoftext|>"
ASSISTANTTOKEN = "<|assistant|>"

def prompt(inp):
    data = {"text":inp}
    headers = {'Content-Type': 'application/json', 'Accept': 'text/plain'}
    response = requests.post(URL, data=json.dumps(data), headers=headers)
    return response.json()["generated_text"]

history = ""
while True: 
    inp = input(">>> ")   
    context = history + USERTOKEN + inp + ENDTOKEN + ASSISTANTTOKEN