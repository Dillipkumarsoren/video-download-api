from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess, json

app = Flask(__name__)
CORS(app)

@app.route("/api")
def api():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "no url"})

    p = subprocess.run(
        ["yt-dlp", "-j", url],
        capture_output=True, text=True
    )

    data = json.loads(p.stdout)
    formats = []

    for f in data["formats"]:
        if f.get("url"):
            formats.append({
                "quality": f.get("format_note", "video"),
                "url": f["url"]
            })

    return jsonify({
        "title": data.get("title"),
        "formats": formats[:5]
    })

app.run(host="0.0.0.0", port=5000)
