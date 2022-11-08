from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route('/aboutme', methods=['GET'])
def about_me():
    return render_template('/mypage/me.html')


@app.route("/", methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        username = request.form["username"]
        comment = request.form["comment"]
        print(f"User {username} wrote {comment}")
    return render_template("/mypage/contact.html")


# ,say=request.form['comment'], to=request.form['username']

if __name__ == "__main__":
    app.run()
