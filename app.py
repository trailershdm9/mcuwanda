from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        link = request.form.get("link")
        return render_template("result.html", link=link)
    return render_template("index.html")

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run()
