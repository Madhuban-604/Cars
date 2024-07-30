from flask import Flask, request

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def post_example():
    data = request.json 