from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
@app.route('/index/<name>')
def index(name="Hello World"):
<<<<<<< HEAD
    return render_template("index.html", text=name)
=======
    return render_template("index.html.jinja", text=name)

>>>>>>> c0eee68a93d3045fc4c9492194fbd6e22de452b0
