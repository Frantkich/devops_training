from flask import Flask
import requests
import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
server = Flask(__name__)
logger = logging.getLogger(__name__)

@server.route('/')
def listBlog():
    logger.debug('Received request to list blog titles')
    rec = requests.get('http://backend-proxy:8081/')
    if not rec:
        logger.error('Failed to retrieve records from backend')
        return '<div> No records found </div>'
    else:
        logger.debug('Successfully retrieved records from backend')
        rec = rec.json().get('titles', [])
    response = ''
    for c in rec:
        response += f'<div>{c}</div>'
    return response


if __name__ == '__main__':
    server.run()