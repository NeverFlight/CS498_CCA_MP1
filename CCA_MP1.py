from urllib import request
from flask import Flask
app = Flask(__name__)
cache = {'num' : 0}
@app.route('/', methods = ['POST', 'GET'])
def handle():
    if request.methods == 'POST':
        cache['num'] = request.json['num']
        return cache
    else:
        return cache

if __name__ == "__main__":
    app.run()