from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    text = request.form.get('user_text', '')
    with open('saved_text.txt', 'w') as f:
        f.write(text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)