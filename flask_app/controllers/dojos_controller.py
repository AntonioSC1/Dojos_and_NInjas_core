from flask_app import app
from flask_app.models.dojo import Dojo
from flask import render_template,redirect,request,session,flash

#read all Route
@app.route("/")
def main_page():
    dojos= Dojo.get_all_dojos()
    return render_template("dojos.html", dojos=dojos)

@app.route("/dojo/create", methods=['POST'])
def create_dojo():
    data={
        "name": request.form['name']
    }
    dojo= Dojo.create_new_dojo(data)
    return redirect("/")


@app.route("/dojo/<int:id>")
def show_dojo(id):
    data={
        "id": id
    }
    dojo= Dojo.get_one_dojo(data)
    return render_template("dojo_info.html", dojo=dojo)