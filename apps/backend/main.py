from flask import Flask
import json
import logging
import os

from dbmanager import DBManager

if os.environ.get('FLASK_DEBUG') == '1':
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)
app = Flask(__name__)
conn = None
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


@app.route('/healthz')
def health():
    logger.debug('Received health check request')
    return 'OK', 200


@app.route('/')
def listBlog():
    logger.debug('Received request to list blog titles')
    global conn
    if not conn:
        conn = DBManager(password=os.environ.get('MARIADB_ROOT_PASSWORD'), host=os.environ.get('MARIADB_HOST'))
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