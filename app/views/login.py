from flask import (
    flash,
    request,
    redirect,
    render_template,
    url_for,
)
from flask_login import login_user

from app import bcrypt
from app.models.user import User
from app.forms.login import LoginForm
from app.utils.decorators import logout_required
from app.views import accounts


@accounts.route("/login", methods=["GET", "POST"])
@logout_required
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(
            user.password, form.password.data
        ):
            login_user(user)
            return redirect(url_for("accounts.hello"))
        else:
            flash("Invalid email/password", "danger")
            return render_template("accounts/login.html", form=form)

    return render_template("accounts/login.html", form=form)
