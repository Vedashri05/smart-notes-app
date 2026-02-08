from flask import Blueprint,request,url_for,session,redirect,render_template,flash
from app import db
from app.models import User
from app.forms import RegistrationForm,LoginForm
from werkzeug.security import generate_password_hash,check_password_hash

auth_bp=Blueprint('auth',__name__)

@auth_bp.route('/login',methods=["GET","POST"])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        username=form.username.data
        password=form.password.data

        existing_user=User.query.filter_by(username=username).first()

        if existing_user and check_password_hash(existing_user.password,password):

            session['user']=username
            if form.remember_me.data:
                session.permanent=True
            else:
                session.permanent=False
            flash("Login sucessful",'success')
            return redirect(url_for("notes.view_notes"))
        else:
            flash("Invalid username or password!",'danger')
    return render_template("login.html",form=form)


@auth_bp.route('/logout')
def logout():
    session.pop('user',None)
    flash("Logout Successfully",'info')
    return redirect(url_for('auth.login'))


@auth_bp.route('/register',methods=["GET","POST"])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        username=form.username.data
        email=form.email.data
        password=form.password.data

        #check email
        existing_user=User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already registered. Please Login",'info')
            return redirect(url_for("auth.login"))
        
        existing_username=User.query.filter_by(username=username).first()
        if existing_username:
            flash("Username already taken, try different",'danger')
            return redirect(url_for("auth.register"))
        
        hashed_password=generate_password_hash(password)
        new_user=User(
            username=username,email=email,
            password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful. Please login",'success')
        return redirect(url_for("auth.login"))

    return render_template("register.html",form=form)
            

