from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from model import db, AdminStaffData

create_staff_bp = Blueprint('create_staff', __name__)

@create_staff_bp.route('/create_staff', methods=['GET', 'POST'])
def create_staff():
    if 'user_id' not in session or session['role'] != 'Admin':
            flash('You must be an admin to access this page.', 'danger')
            return redirect(url_for('login.login'))
    
    
    if request.method == 'POST':
        username = request.form['username']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        role = request.form['role']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        zipcode = request.form['zipcode']
        password = request.form['password']

        existing_staff = AdminStaffData.query.filter(
            (AdminStaffData.username == username) | (AdminStaffData.email == email)
        ).first()

        if existing_staff:
            flash('A staff member with this username or email already exists.', 'danger')
            return redirect(url_for('create_staff.create_staff'))

        new_staff = AdminStaffData(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            role=role,
            address=address,
            city=city,
            state=state,
            zipcode=zipcode,
            password=password
        )

        db.session.add(new_staff)
        db.session.commit()

        if role == 'Staff':
            flash('Staff member created successfully.', 'success')
        elif role == 'Admin':
            flash('Admin was created successfully.', 'success')

        return redirect(url_for('create_staff.create_staff'))

    return render_template('create_staff.html')
