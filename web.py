from flask import Flask, request, jsonify
from lib.webdriver import Webdriver

app = Flask(__name__)

@app.route("/retrieve", methods=['POST'])
def retrieve():
    webdriver = Webdriver()
    content = request.json
    url = content['url']
    return webdriver.get_url(url)

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)