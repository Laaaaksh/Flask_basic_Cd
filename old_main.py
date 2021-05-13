from flask import Flask, request

app=Flask(__name__) #to help it determine the root path
#routing can be done using a decorator , it is @symbol - it is a decorator
#forward slash is the root directory, this is routing or mapping
@app.route('/')
def index():
    return 'Method used %s' % request.method
#default method used is get
#we need to use post when we are working with forms

@app.route('/bacon', methods=['GET', 'POST'])
def bacon():
    if request.method=='POST':
        return "You are using Post"
    else:
        return "You are still using GIT"

# @app.route('/tuna')
# def tuna():
#     return '<h2> Tuna is good</h2>'

# @app.route('/profile/<username>') #we will take run time variable
# def profile(username):
#     return "Hello %s" %username

# #if you use, any different data types than string, we need to specify the data type
# @app.route('/post/<int:post_id>')  # we will take run time variable
# def post(post_id):
#     return "Hello %s" % post_id

if __name__== "__main__":
    app.run(debug=True)
#run the main app only when this file is scripted
