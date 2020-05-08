from flask import Flask
import os


app = Flask(__name__)
namespace = os.getenv("namespace")
worker_host = "pong" + namespace

@app.route("/")
def backend():
    r = requests.get("http://"+worker_host)
    worker = socket.gethostbyname(worker_host)
    return "Pong Message: {}\nFrom: {}".format(r.content, worker)


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=True, port=8081)
