from flask import render_template, request, redirect, url_for
from . import db, app
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

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home"))