import threading
from concurrent.futures import ThreadPoolExecutor
from flask import Flask, request

from lib.webdriver import Webdriver

class WebdriverPool:
    def __init__(self, size):
        self.size = size
        self.pool = [Webdriver() for _ in range(size)]
        self.used_objects = set()
        self.condition = threading.Condition()

    def wait_and_acquire(self):
        with self.condition:
            while len(self.pool) == 0:
                self.condition.wait()
            obj = self.pool.pop()
            self.used_objects.add(obj)
            return obj

    def release(self, obj):
        with self.condition:
            if obj in self.used_objects:
                self.used_objects.remove(obj)
                self.pool.append(obj)
                self.condition.notify()

    def __len__(self):
        return len(self.pool)


executor = ThreadPoolExecutor()
app = Flask(__name__)
pool = WebdriverPool(5)

def scraping_function(url, cookies):
    webdriver = pool.wait_and_acquire()
    result = webdriver.get_url(url, cookies)
    pool.release(webdriver)
    return result

@app.route("/retrieve", methods=['POST'])
def retrieve():
    content = request.json
    url = content['url']
    cookies = content.get('cookies', [])
    future = executor.submit(scraping_function, url, cookies)
    result = future.result()
    return result


if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)