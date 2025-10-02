from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

videos = [
    {"title": "Video relajante", "thumbnail": "/static/assets/videos/video1.png"},
    {"title": "Pop clásico", "thumbnail": "/static/assets/videos/video2.png"},
    {"title": "Rock suave", "thumbnail": "/static/assets/videos/video3.png"}
]

tags = {
    "Video relajante": ["relajante", "estudio", "calma"],
    "Pop clásico": ["pop", "clásico", "fiesta"],
    "Rock suave": ["rock", "suave", "relajante"]
}

summaries = {
    "Video relajante": "Canción perfecta para estudiar o relajarse.",
    "Pop clásico": "Pop clásico de los 80s ideal para animarte.",
    "Rock suave": "Rock suave, perfecto para escuchar tranquilo."
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    query = request.json.get("query", "").lower()
    recommended = []
    for video in videos:
        title = video["title"].lower()
        video_tags = [t.lower() for t in tags.get(video["title"], [])]
        if query in title or query in video_tags:
            video_copy = video.copy()
            video_copy["summary"] = summaries.get(video["title"], "")
            recommended.append(video_copy)
    return jsonify(recommended)

@app.route("/playlists", methods=["GET"])
def playlists():
    generated_playlists = {
        "Estudio": ["Video relajante", "Rock suave"],
        "Fiesta": ["Pop clásico"],
        "Relax": ["Video relajante", "Rock suave"]
    }
    return jsonify(generated_playlists)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
