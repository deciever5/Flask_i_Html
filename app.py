from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/aboutme', methods=['GET'])
def about_me():
    return render_template('/mypage/me.html')


@app.route("/", methods=['GET', 'POST'])
def contact():
    return render_template("/mypage/contact.html")


if __name__ == "__main__":
    app.run()
