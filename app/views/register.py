from flask import (
    flash,
    jsonify,
    make_response,
    request,
    redirect,
    render_template,
    url_for,
)
from flask_login import login_user

from app import db
from app.models.user import User
from app.forms.register import RegisterForm
from app.utils.decorators import logout_required
from app.views import accounts


@accounts.route("/")
def hello():
    users = User.query.all()
    return make_response(jsonify([user.to_dict() for user in users]))


@accounts.route("/register", methods=["GET", "POST"])
@logout_required
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )
        db.session.add(user)
        db.session.commit()

        # token = generate_token(user.email)
        # confirm_url = url_for(
        #     "accounts.confirm_email", token=token, _external=True
        # )
        # html = render_template(
        #     "accounts/confirm_email.html", confirm_url=confirm_url
        # )
        # subject = "Please confirm your email"
        # send_email(user.email, subject, html)

        login_user(user)
        # flash("A confirmation email has been sent via email", "success")

        # return redirect(url_for("accounts.inactive"))
        return redirect(url_for("accounts.login"))

    return render_template("accounts/register.html", form=form)
