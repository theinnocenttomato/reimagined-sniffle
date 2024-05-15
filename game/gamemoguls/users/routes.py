from flask import blueprints, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from gamemoguls.users.forms import RegistrationForm, LoginForm, resetPasswordForm, newPasswordForm
from gamemoguls import db, mail,login_manager
from gamemoguls.models import Users

users = blueprints.Blueprint('users', __name__)

@login_manager.user_loader
def load_user(user_id):
    """
    Load a user from the database using the user_id
    """
    return Users.query.get(int(user_id))

@users.route('/login', methods=['GET', 'POST'])
def login():
    """
    Log in a user
    """
    form = LoginForm()

    if form.validate_on_submit():
        # Check if the email and password match a user in the database
        user = Users.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('main.index'))

        flash('Invalid email or password', 'error')

    return render_template('users/login.html', form=form)

@users.route('/register' , methods=['GET', 'POST'])
def register():
    """
    Register a new user
    """
    form = RegistrationForm()

    if form.validate_on_submit():
        # Hash the password before storing it in the database
        hashed_password = generate_password_hash(form.password.data, method='scrypt')

        # Create a new User object with the form data and add it to the database
        new_user = Users(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Your account has been created! You are now able to log in.', 'success')
        return redirect(url_for('users.login'))

    return render_template('users/register.html', title='Register', form=form)

@users.route('/profile')
@login_required
def profile():

    return render_template('users/profile.html')

@users.route('/logout')
@login_required
def logout():
    """
    Log out the current user
    """
    logout_user()
    return redirect(url_for('main.index'))

@users.route('/resetPassword', methods=['GET', 'POST'])
def reset_request(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = resetPasswordForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            flash('If an account exists with that email, a reset link has been sent to your email', 'info')
        else:
            token = Users.get_reset_token(user)
            mail.send_message('Password Reset Request',
                              
            )
            flash('If an account exists with that email, a reset link has been sent to your email', 'info')
        
    return render_template('users/resetPassword.html', form=form)

@users.route('/resetPassword/<token>', methods=['GET', 'POST'])
def resetpassword(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = Users.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('users.reset_request'))
    form = newPasswordForm()

    return render_template('users/newPassword.html', form=form)
