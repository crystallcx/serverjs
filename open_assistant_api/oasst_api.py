from flask import Flask, jsonify, request
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

import os

app = Flask(__name__)

MODEL_NAME = "OpenAssistant/osst-sft-4-pythia-12b-epoch-3.5"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

model = model.half()

@app.route('/generate', methods=['POST'])
def generate():
    content = request.json
    inp = content.get("test", "")
    input_ids = tokenizer.encode(inp, return_tensors="pt")
    with torch.cuda.amp.autocast():
        outputs = model.generate(input_ids, max_length=2048, do_sample=True, early_stopping=True)
        output = output.cpu()
        
    decoded_output = tokenizer.decode(output[0], skip_special_tokens=False)
    return jsonify({"generated_text": decoded_output})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)