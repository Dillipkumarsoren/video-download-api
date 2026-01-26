from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess, json, os

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return "API is running"

@app.route("/api", methods=["GET"])
def api():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "no url provided"})

    p = subprocess.run(
        ["yt-dlp", "-j", url],
        capture_output=True,
        text=True
    )

    if p.returncode != 0:
        return jsonify({
            "error": "yt-dlp failed",
            "details": p.stderr
        })

    data = json.loads(p.stdout)
    formats = []

    for f in data.get("formats", []):
        if f.get("url"):
            formats.append({
                "quality": f.get("format_note", "video"),
                "url": f["url"]
            })

    return jsonify({
        "title": data.get("title"),
        "formats": formats[:5]
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
