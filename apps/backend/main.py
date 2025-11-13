from flask import Flask, request
import json
import logging
import os

from flask_cors import CORS

from dbmanager import DBManager

if os.environ.get("FLASK_DEBUG") == "1":
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)
app = Flask(__name__)
CORS(app)
conn = None
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")


@app.route("/healthz")
def health():
    logger.debug("Received health check request")
    return "OK", 200


@app.route("/api/blogs", methods=["GET", "POST"])
def listBlog():
    global conn
    if not conn:
        # conn = DBManager(password=os.environ.get('MARIADB_ROOT_PASSWORD'), host=os.environ.get('MARIADB_HOST'))
        conn = DBManager()
        conn.populate_db()
    if request.method == "POST":
        logger.debug("Received request to add blog title")
        conn.append_title(request.json.get("title"))
        return json.dumps({"message": "Title added successfully"}), 201
    if request.method == "GET":
        logger.debug("Received request to list blog titles")
        rec = conn.query_titles()
        titles = []
        for c in rec:
            titles.append(c)
        return json.dumps({"message": "Here are the blog titles", "titles": titles})


if __name__ == "__main__":
    app.run()
