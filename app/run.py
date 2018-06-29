from flask import Flask

app = Flask(__name__)


@app.route('/home')
def index():
    return "hello blue"

if __name__ == '__main__':
    app.run()