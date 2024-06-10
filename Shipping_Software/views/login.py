from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from model import GeneralUser, AdminStaffData

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        general_user = GeneralUser.query.filter_by(username=username).first()
        admin_staff_user = AdminStaffData.query.filter_by(username=username).first()

        if general_user and password == general_user.password:
            session['user_id'] = general_user.id
            flash('Congratulations, you\'ve successfully logged in! Time to get to work!', 'success')
            return redirect(url_for('dashboard.dashboard'))
        elif admin_staff_user and password == admin_staff_user.password:
            session['user_id'] = admin_staff_user.id
            session['role'] = admin_staff_user.role
            flash('Congratulations, you\'ve successfully logged in! Time to get to work!', 'success')
            if admin_staff_user.role == 'Admin':
                return redirect(url_for('admin_dashboard.admin_dashboard'))
            elif admin_staff_user.role == 'Staff':
                return redirect(url_for('staff_dashboard.staff_dashboard'))
        else:
            flash('Oh no, it looks like your username or password is incorrect. Give it another shot!', 'failed')

    return render_template('login.html')
