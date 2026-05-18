# app.py

from flask import Flask, render_template, jsonify
import psutil
from datetime import datetime

app = Flask(__name__)

# Home Page
@app.route("/")
def dashboard():
    return render_template("index.html")


# API Route for System Stats
@app.route("/stats")
def stats():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    data = {
        "cpu": cpu,
        "ram_percent": ram.percent,
        "ram_used": round(ram.used / (1024 ** 3), 2),
        "ram_total": round(ram.total / (1024 ** 3), 2),
        "disk_percent": disk.percent,
        "disk_used": round(disk.used / (1024 ** 3), 2),
        "disk_total": round(disk.total / (1024 ** 3), 2),
        "time": datetime.now().strftime("%H:%M:%S")
    }

    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)