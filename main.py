from flask import Flask
from obswebsocket import obsws, requests

ws = obsws("localhost", 4455, "YOUR_PASSWORD")
ws.connect()

app = Flask(__name__)

@app.route("/scene", methods=["POST"])
def change_scene():
    ws.call(requests.SetCurrentProgramScene(sceneName="Final"))
    return "OK"

app.run(host="0.0.0.0", port=5000)
