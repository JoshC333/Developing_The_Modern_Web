from flask import Flask, make_response, abort, redirect

app = Flask(__name__);

@app.route('/')
def hello_world():
    return redirect('https://preview.c9users.io/joshcoulsell/developing_modern_web_submission/index.html')

@app.route('/users/<username>')
def hello_me(username):
    return 'Hello ' + username + '!'
    
@app.route('/error')
@app.route('/errors')
def error():
    return redirect('https://preview.c9users.io/joshcoulsell/developing_modern_web_submission/error.html?_c9_id=livepreview2&_c9_host=https://ide.c9.io')


@app.route('/unexpected')
def unexpected():
    abort(404)
    return True

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0', debug=True)