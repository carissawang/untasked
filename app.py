from flask import Flask, render_template, request, redirect, url_for, session
import datetime
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/surveypage1', methods=["POST", "GET"])
def firstsurveypart1():
    if request.method == "GET":
        return render_template("survey.html")
    elif request.method == "POST":
        result = request.form
        session["Username"] = result["Name"]
        return render_template("survey2.html", name=result["Name"])
    else:
        pass



#replace surveyresponse with audreys dashboard
@app.route('/surveypage2', methods=["POST", "GET"])
def firstsurveypart2():
    if request.method == "GET":
        return render_template("survey2.html")
    elif request.method == "POST":
        result2 = request.form
        return redirect("/dashboard")
    else:
        pass


@app.route('/dashboard')
def dashboard():
    print session["Username"]
    return render_template("productivity.html", name = session["Username"])

@app.route('/todolist', methods=["POST", "GET"])
def todolist():
    if request.method == "GET":
        session["todos"] = ()
        return render_template("calendar.html")
    else:
        todo = request.form["todo"]

        print "adding todos"
        if "todos" in session:
            todo_list = list(session["todos"])
            todo_list.append(todo)
            session["todos"] = todo_list
        else:
            session["todos"] = (todo)

        todo_list = session["todos"]
        return render_template("calendar.html", todos = todo_list)
