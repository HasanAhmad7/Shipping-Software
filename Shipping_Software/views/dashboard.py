from flask import Blueprint, render_template, redirect, url_for, flash, session, request
from model import db, GeneralUser, GeneralQuotation

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Hold your horses! You need to log in first to see this page.', 'info')
        return redirect(url_for('login.login'))
    
    user_id = session['user_id']
    user = GeneralUser.query.get(user_id)
    
    if 'role' in session and session['role'] in ['Staff', 'Admin']:
        flash('Oops! Looks like you took a wrong turn on the Admin or Staff highway. No entry to the General User dashboard for you!', 'failed')
        return redirect(url_for('login.login'))
    
    # Pagination
    page = request.args.get('page', 1, type=int)
    per_page = 5
    user_quotations = GeneralQuotation.query.filter_by(created_by=user.username).paginate(page=page, per_page=per_page, error_out=False)
    
    return render_template('dashboard.html', user=user, user_quotations=user_quotations)
