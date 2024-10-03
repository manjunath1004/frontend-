from flask import Flask

app = Flask(__name__)


@app.route('/about')
def index():
    return 'Hello from Flask mani!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debuge=True)
