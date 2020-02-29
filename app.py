from flask import Flask, render_template, redirect, make_response
# from flask import jsonify



app = Flask(__name__)


@app.route("/")
@app.route("/main")
def home():
    return render_template('main.html', title='Twit Stack')


   
    
if __name__ == "__main__":
    app.run(debug=True)

