from flask import Blueprint, flash, redirect, render_template, session, url_for
from model import AdminStaffData

staff_dashboard_bp = Blueprint('staff_dashboard', __name__)

@staff_dashboard_bp.route('/staff_dashboard')
def staff_dashboard():
    if 'user_id' not in session:
        flash('Oops! Looks like you need a VIP pass to enter this area. Staff only, please!', 'info')
        return redirect(url_for('login.login'))
    
    if 'role' not in session or session['role'] != 'Staff':
        flash('Ah, ah, ah! You need to be a staff member to access this page. No sneak peeks allowed!', 'failed')
        return redirect(url_for('login.login'))
    
    user_id = session['user_id']
    staff_member = AdminStaffData.query.get(user_id)

    if not staff_member or staff_member.role != 'Staff':
        flash('Ah, ah, ah! You need to be a staff member to access this page. No sneak peeks allowed!', 'failed')
        return redirect(url_for('login.login'))
    
    return render_template('staff_dashboard.html', user=staff_member)