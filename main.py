from flask import Flask, jsonify
from flask_cors import CORS
import psutil

app = Flask(__name__)
CORS(app)  # allow React to access

@app.route("/api/cpu", methods=["GET"])
def cpu_usage():
    cpu = psutil.cpu_percent(interval=1)
    return jsonify({"cpu_load": cpu})

@app.route("/api/memory", methods=["GET"])
def memory_usage():
    memory = psutil.virtual_memory()
    return jsonify({
        "memory_total": round(memory.total / (1024 * 1024), 2),
        "memory_used": round(memory.used / (1024 * 1024), 2)
    })

@app.route("/api/disk", methods=["GET"])
def disk_usage():
    disk = psutil.disk_usage('/')
    return jsonify({
        "disk_total": round(disk.total / (1024 * 1024), 2),
        "disk_used": round(disk.used / (1024 * 1024), 2),
        "disk_percent": disk.percent
    })

if __name__ == "__main__":
    app.run(debug=True)
