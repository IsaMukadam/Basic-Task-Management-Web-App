from flask import render_template, request, redirect, url_for
from . import db, app  # Import the app instance here
from .models import Task

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task_content = request.form.get("task")
        if task_content:
            new_task = Task(content=task_content)
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for("home"))

    tasks = Task.query.all()
    return render_template("home.html", tasks=tasks)
