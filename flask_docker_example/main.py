from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def hello_world():
    return "Welcome to about page!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

