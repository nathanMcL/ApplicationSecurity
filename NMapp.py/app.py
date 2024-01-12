from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    input_data = request.form['inputField']
    # Process input_data as needed
    return "Received: " + input_data


if __name__ == "__main__":
    app.run(debug=True)
