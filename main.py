from flask import Flask, render_template
app= Flask(__name__)

#how to map 2 different urls to the same function
@app.route("/")
@app.route("/<user>")
def index(user=None):
    return render_template("user.html", user=user)

@app.route('/list')
def list_():
    food= ["Cheese", "Tuna", "Chicken"]
    return render_template("list.html", food=food)

# @app.route('/')
# def index():
#     return "Hey you are back on the Home page"

# @app.route('/profile/<name>')
# def profile(name):
#     return render_template("profile.html", name=name)


if __name__ == '__main__':
    app.run(debug=True)