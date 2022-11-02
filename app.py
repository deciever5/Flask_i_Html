from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask(__name__)


@app.route('/')
def hello():
    my_name = "John"
    return f'Hello, {my_name}!'


@app.route('/blog/<id>')
def blog_main(id):
    return f"This is a  blog entry #{id}"


@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'GET':
        print("We received GET")
        return render_template("form.html")
    elif request.method == 'POST':
        print("We received POST")
        print(request.form)
        return redirect("/")
