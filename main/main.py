from flask import Flask

app=Flask(__name__) #to help it determine the root path
#routing can be done using a decorator , it is @symbol - it is a decorator
@app.route('/') #forward slash is the root directory, this is routing or mapping
def index():
    return 'This is the Home page'

@app.route('/tuna')
def tuna():
    return '<h2> Tuna is good</h2>'

@app.route('/profile/<username>') #we will take run time variable
def profile(username):
    return "Hello %s" %username

#if you use, any different data types than string, we need to specify the data type
@app.route('/post/<int:post_id>')  # we will take run time variable
def post(post_id):
    return "Hello %s" % post_id

if __name__== "__main__":
    app.run(debug=True)
    #run the main app only when this file is scripted
