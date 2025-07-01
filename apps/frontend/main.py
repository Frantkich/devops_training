from flask import Flask
import requests
import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
app = Flask(__name__)
logger = logging.getLogger(__name__)

@app.route('/healthz')
def health():
    logger.debug('Received health check request')
    return 'OK', 200


@app.route('/')
def listBlog():
    logger.debug('Received request to list blog titles')
    try:
        rec = requests.get('http://backend-proxy:8081/')
    except requests.exceptions.ConnectionError as e:
        rec = None
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
    app.run()