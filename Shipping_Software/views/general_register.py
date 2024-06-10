from flask import Blueprint, render_template, request, redirect, url_for, flash
from model import db
from model import GeneralUser

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        phone_number = request.form['phone_number']
        password = request.form['password']

        existing_user = GeneralUser.query.filter_by(username=username).first()
        if existing_user:
            flash('User already exists', 'failed')
            return redirect(url_for('register.register'))

        # Create new user
        new_user = GeneralUser(username=username, email=email, phone_number=phone_number, password=password)

        db.session.add(new_user)
        db.session.commit()
        flash('User created successfully', 'success')
        return redirect(url_for('login.login'))

    return render_template('register.html')
