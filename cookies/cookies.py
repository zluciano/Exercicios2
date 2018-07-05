from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def home():
    resp = make_response(render_template('home.html'))
    resp.set_cookie('name', 'I am cookie')
    return resp

@app.route('/get-cookie/')
def get_cookie():
    username = request.cookies.get('username')

if __name__ == '__main__':
    app.run(debug=True)
