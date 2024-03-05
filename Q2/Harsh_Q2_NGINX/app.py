from transformers import pipeline, AutoTokenizer, TFAutoModelForSeq2SeqLM
from flask import Flask, request, jsonify

app = Flask(__name__)

model_path = 'models/transformers/' 
model_name = "Falconsai/text_summarization"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = TFAutoModelForSeq2SeqLM.from_pretrained(model_name)

summarizer = pipeline('summarization', model=model, tokenizer=tokenizer)

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    text = data['text']
    summary = summarizer(text, max_length=150, min_length=40, do_sample=False)[0]['summary_text']
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
