from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "API is running"

@app.route("/download")
def download():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "URL not provided"})

    return jsonify({
        "status": "success",
        "video_url": url
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
