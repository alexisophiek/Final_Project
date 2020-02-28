from flask import Flask, render_template, redirect, make_response
from flask import jsonify

import basics


app = Flask(__name__)


@app.route("/")
@app.route("/main")
def home():
    return render_template('main.html', title='Twit Stack')



# @app.route("/about")
# def about():
#     print("Server received request for 'About' page...")
#     return "Welcome to my 'About' page!"


if __name__ == "__main__":
    app.run(debug=True)

