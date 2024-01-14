from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    input_data = request.form['inputField']
    # Render the result template with the input data
    return render_template("results.html", submitted_data=input_data)


if __name__ == "__main__":
    app.run(debug=True)
