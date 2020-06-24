from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
  return '<h1>I am HOME</h1>'


