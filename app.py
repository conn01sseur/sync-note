from flask import Flask, request, render_template
from datetime import datetime
import os

app = Flask(__name__)
current_datetime = datetime.now()
formatted_date = current_datetime.strftime("%m.%d")
num = 154

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