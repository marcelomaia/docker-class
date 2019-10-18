import argparse
import random
import socket

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    with open('quotes.txt', 'r') as f:
        quotes = f.read().split('¬')
    return f"Hello {socket.gethostname()}. \n{random.choice(quotes)}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", action="store", default="8000")

    args = parser.parse_args()
    port = int(args.port)

    app.run(host="0.0.0.0", port=port)
