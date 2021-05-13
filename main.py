from flask import Flask, render_template
app= Flask(__name__)

@app.route('/')
def index():
    return "Hey you are back on the Home page"

@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html", name=name)


if __name__ == '__main__':
    app.run(debug=True)