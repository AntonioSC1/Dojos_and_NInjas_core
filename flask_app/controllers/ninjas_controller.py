from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
from flask import render_template,redirect,request,session,flash

#route to create Ninja Page
@app.route("/ninjas")
def ninja_page():
    dojos= Dojo.get_all_dojos()
    return render_template("ninjas.html", dojos=dojos)

#create method for New Ninjas
@app.route("/ninja/create", methods=["POST"])
def create_ninja():
    print("form data:", request.form)
    data = {
        'dojos_id': request.form['dojo_id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }
    Ninja.create_ninja(data)
    return redirect(f"/dojo/{data['dojos_id']}")