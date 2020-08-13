import configparser 
import asyncio
from app.server import HealthCheck, GetRecords
from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from collections import defaultdict

objApi = defaultdict(dict)
# Uncomment if running in a windows env
# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

def store_in_objApi(key, value):
    objApi[key] = value

def init_api():
    config = configparser.ConfigParser()
    config.read('app/config/config.ini')
    config_env = config.items('dev')
    config_dict = dict((x, y) for x, y in config_env)
    store_in_objApi("config", config_dict)


def create_api():
    global objApi
    init_api()
    urls = [
        ("/health-check", HealthCheck, dict(objApi=objApi)),
        ("/records", GetRecords, dict(objApi=objApi))
    ]
    return Application(urls)
  
if __name__ == '__main__':
    print("Listening...")
    app = create_api()
    http_server = HTTPServer(app)
    http_server.listen(8080)
    IOLoop.current().start()