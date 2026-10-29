from flask import Flask, jsonify
import os
app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/version")
def version():
    return jsonify({"version": os.environ.get('APP_VERSION', 'dev')})

if __name__ == "__main__":
    app.run(debug=True)

