from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db 
from flask_login import login_user, login_required, logout_user, current_user
from .Wykresy import W1, W2, W3, W4

auth = Blueprint('auth', __name__)


@auth.route('/')
def start():
    return render_template('/home.html',user=current_user)

@auth.route('/home')
def home():
    return render_template('/home.html',user=current_user)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Zalogowano poprawnie!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('auth.home'))
            else:
                flash('Złe hasło.Zaloguj się ponownie', category='error')
        else:
            flash('Email nie istnieje.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))



@auth.route('/dane')
def dane():
    chart_data = generate_chart()
    return render_template('dane.html',user=current_user, chart_data=chart_data)


@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email istnieje.', category='error')
        elif password1 != password2:
            flash('Hasła nie pasują', category='error')
        elif len(password1) < 5:
            flash('Hsało musi posiadać minimum 5 zanków.', category='error')
        else:
            new_user = User(email=email, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Konto założone', category='success')
            return redirect(url_for('auth.home'))

    return render_template("sign_up.html", user=current_user)

@auth.route('/chart', methods=['POST'])
def generate_chart():
        chart_id = request.form.get('chartId')

        if chart_id == 'benzyna':
            chart = W1()
        elif chart_id == 'olej':
            chart = W2()
        elif chart_id == 'gaz':
            chart = W3()
        elif chart_id == 'pozostale':
            chart = W4()
        else:
            response = {'status': 'OK'}
            return jsonify(response)
