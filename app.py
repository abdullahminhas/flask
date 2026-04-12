from flask import Flask, render_template

app = Flask(__name__)

# Route for home page
@app.route("/")
def home():
    # Render the template 'index.html' and pass a variable
    return render_template("index.html", name="World")

if __name__ == "__main__":
    app.run(debug=True)
