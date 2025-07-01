from flask import Flask
import json
import logging

from dbmanager import DBManager


logger = logging.getLogger(__name__)
app = Flask(__name__)
conn = None
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


@app.route('/health')
def health():
    logger.debug('Received health check request')
    return 'OK', 200


@app.route('/')
def listBlog():
    logger.debug('Received request to list blog titles')
    global conn
    if not conn:
        conn = DBManager(password_file='/run/secrets/db-password')
        conn.populate_db()
    rec = conn.query_titles()

    titles = []
    for c in rec:
        titles.append(c)
    return json.dumps({
        "message": "Here are the blog titles",
        "titles": titles
    })


if __name__ == '__main__':
    app.run()