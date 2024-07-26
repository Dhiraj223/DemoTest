from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hope it works!'

if __name__ == '__main__':
    app.run()