from .logger import Logger

import requests

"""HTTP methods list"""


class HttpMethods:
    headers = {"Content-Type": "application/json"}
    cookie = ""

    @staticmethod
    def get(url):
        Logger.add_request(url, method="GET")
        result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def post(url, body):
        Logger.add_request(url, method="POST")
        result = requests.post(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie, json=body)
        Logger.add_response(result)
        return result

    @staticmethod
    def put(url, body):
        Logger.add_request(url, method="PUT")
        result = requests.put(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie, json=body)
        Logger.add_response(result)
        return result

    @staticmethod
    def delete(url, body):
        Logger.add_request(url, method="DELETE")
        result = requests.delete(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie, json=body)
        Logger.add_response(result)
        return result


