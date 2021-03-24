from flask import Flask ,render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        ad = request.form["ad"]
        soyad = request.form["soyad"]
        if request.form["button"] == "Go to page 2":
            return redirect(url_for("page_2", ad=ad, soyad=soyad))

    return render_template("index.html")


@app.route("/page_2", methods=["GET"])
def page_2():
    ad = request.args.get("ad")
    soyad = request.args.get("soyad")
    return render_template("page_2.html", ad=ad,
                           soyad=soyad)

if __name__ == "__main__":
    app.run(debug=True)
