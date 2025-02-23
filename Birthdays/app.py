from flask import Flask, render_template, request , redirect

from cs50 import SQL 

app = Flask(__name__)

db = SQL("sqlite:///birthdays.db")


@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        day = request.form.get("day")
        month = request.form.get("month")
        year = request.form.get("year")
        if not name or not day or not month or not year:
            return redirect("/")
        
        db.execute("INSERT INTO birthdays (name , day , month , year) VALUES (?,?,?,?)",name,day,month,year)
        return redirect("/")
    else:
     rows = db.execute("SELECT * FROM birthdays")
     return render_template("index.html",birthdays = rows)