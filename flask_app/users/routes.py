from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash
)
from flask_login import(
    current_user,
    login_user,
    logout_user,
    login_required
)
from flask_app.forms import(
    LoginForm
)
from flask_app.models import User
from flask_app import bcrypt

users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("homepage.index"))
    
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.objects(username=login_form.username.data).first()
        if user is not None and bcrypt.check_password_hash(
            user.password, login_form.password.data
        ):
            login_user(user)
            return redirect(url_for("homepage.index"))
        else:
            flash("username or password incorrect")
            return redirect(url_for("users.login"))
    
    return render_template("login.html", form=login_form)


@users_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("users.login"))