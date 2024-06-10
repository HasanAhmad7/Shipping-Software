from flask import Blueprint, render_template, redirect, url_for, flash, session
from model import AdminStaffData

admin_dashboard_bp = Blueprint('admin_dashboard', __name__)

@admin_dashboard_bp.route('/admin_dashboard')
def admin_dashboard():
    if 'user_id' not in session:
        flash('Oops! Looks like you need a VIP pass to enter this area. Admins only, please!', 'info')
        return redirect(url_for('login.login'))
    
    if 'role' not in session or session['role'] != 'Admin':
        flash('Ah, ah, ah! You need to be an admin to access this page. No sneak peeks allowed!', 'failed')
        return redirect(url_for('login.login'))
    
    user_id = session['user_id']
    admin_user = AdminStaffData.query.get(user_id)
    
    if not admin_user or admin_user.role != 'Admin':
        flash('Ah, ah, ah! You need to be an admin to access this page. No sneak peeks allowed!', 'failed')
        return redirect(url_for('login.login'))
    
    return render_template('admin_dashboard.html', user=admin_user)
