from flask import Flask, request, render_template
from datetime import datetime
import os
import json

app = Flask(__name__)

COUNTER_FILE = 'counter.json'

def load_counter():
    try:
        with open(COUNTER_FILE, 'r') as f:
            data = json.load(f)
            return data['num'], datetime.strptime(data['last_date'], "%m.%d")
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        return 155, datetime.now()

def save_counter(num, date):
    with open(COUNTER_FILE, 'w') as f:
        json.dump({'num': num, 'last_date': date.strftime("%m.%d")}, f)

current_datetime = datetime.now()
formatted_date = current_datetime.strftime("%m.%d")
num, last_date = load_counter()

if formatted_date != last_date.strftime("%m.%d"):
    num += 1
    save_counter(num, current_datetime)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    text = request.form.get('user_text', '')
    os.makedirs(f"notes/{formatted_date} ({num})", exist_ok=True)
    with open(f'notes/{formatted_date} ({num})/Отчет.md', 'w') as f:
        f.write(text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)