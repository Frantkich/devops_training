from flask import Flask
import requests

server = Flask(__name__)

@server.route('/')
def listBlog():
    rec = requests.get('http://backend-proxy:8081/')
    if not rec:
        return '<div> No records found </div>'
    else:
        rec = rec.json().get('titles', [])
    response = ''
    for c in rec:
        response += f'<div>{c}</div>'
    return response
if __name__ == '__main__':
    server.run()