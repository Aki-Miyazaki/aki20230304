from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/greet')
def greet():
    return 'こんにちは！'

if __name__ == "__main__":
    # Flaskが持っているアプリを実行します-
    app.run(port=8888,debug=True)