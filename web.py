from flask import Flask, request, jsonify
from lib.webdriver import Webdriver

app = Flask(__name__)
webdriver = Webdriver()

@app.route("/retrieve", methods=['POST'])
def retrieve():
    content = request.json
    url = content['url']
    return webdriver.get_url(url)

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)