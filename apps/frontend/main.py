from flask import Flask, render_template
import requests
import logging
import os

if os.environ.get("FLASK_DEBUG") == "1":
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

app = Flask(__name__)
logger = logging.getLogger(__name__)

BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:5000")


@app.route("/healthz")
def health():
    logger.debug("Received health check request")
    return "OK", 200


@app.route("/")
def listBlog():
    logger.debug("Received request to list blog titles")
    return render_template("index.html", BACKEND_URL=BACKEND_URL)


if __name__ == "__main__":
    app.run()
