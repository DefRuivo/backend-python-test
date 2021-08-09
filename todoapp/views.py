from flask import render_template, redirect, url_for, flash, Blueprint
from flask_login import login_user, login_required, logout_user, current_user
from flask_login.utils import login_required
from todoapp.forms.signupform import SignupForm
from todoapp.forms.todoform import TodoForm
from todoapp.forms.loginform import LoginForm
from todoapp.models.model import Todo, User, db
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint("bp", __name__, template_folder="templates", static_url_path="/static")


@bp.route("/", methods=["GET", "POST"])
@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("bp.todolist"))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash(message="Welcome, {}".format(form.username.data), category="sucess")
            return redirect(url_for("bp.todolist"))

    return render_template("login.html", form=form)

@bp.route("/todolist", methods=["GET"])
@login_required
def todolist():
    form = TodoForm()
    todos = Todo.query.filter_by(user_id=current_user.get_id()).all()
    return render_template("todolist.html", form=form, todos=todos)

@bp.route("/todolist", methods=["POST"])
@login_required
def todolist_post():
    form = TodoForm()
    
    if form.validate_on_submit():
        todo = Todo(description=form.description.data, user_id=current_user.get_id())
        
        try:
            db.session.add(todo)
            db.session.commit()
        except:
            flash(message="Cant add this!", category="warning")
            
        return redirect(url_for("bp.todolist"))
    
    return redirect(url_for("bp.todolist"))

@bp.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect(url_for("bp.todolist"))
    except:
        flash(message="You cant delete this!", category="warning")

@bp.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        hashed_pw = generate_password_hash(form.password.data, method="sha256")
        username_data = form.username.data
        add_this = User(username=username_data, password=hashed_pw)
        
        try:
            db.session.add(add_this)
            db.session.commit()
        except:
            flash(message="Error at signing up!", category="danger")
            return redirect(url_for("bp.signup"))
            
        flash(message="Signed up! Please enter your login", category="sucess")
        return redirect(url_for("bp.login"))
    
    return render_template("signup.html", form=form)

@bp.route("/logout")
def logout():
    flash(message="You have logged out!", category="sucess")
    logout_user()
    return redirect(url_for("bp.login"))