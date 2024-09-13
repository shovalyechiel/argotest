from flask import Flask, request, jsonify
import redis
import os


r = redis.Redis(host=os.getenv("REDIS_HOST"), port=os.getenv("REDIS_PORT"))
app = Flask(__name__)


@app.route("/cache", methods=["GET"])
def hello_get():
    key = request.args.get("key", "")
    return jsonify({key: r.get(key)})


@app.route("/cache", methods=["POST"])
def hello_post():
    key = request.args.get("key", "")
    data = request.json
    key = data.get("key", "") if data else ""
    value = data.get("value", "") if data else ""
    r.set(key, value, ttl=60 * 60)
    return jsonify({"message": "OK"})


if __name__ == "__main__":
    app.run(debug=True)
