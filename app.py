from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask(__name__)


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




@app.route('/o_mnie')
def o_mnie():
    return render_template('/wizytowka/o_mnie.html')


@app.route("/")
def warehouse():
    items = ["screwdriver", "hammer", "saw"]
    errors = ["hammer is broken!"]
    return render_template("warehouse.html", items=items, errors=errors)
