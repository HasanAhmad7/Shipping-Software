from flask import Blueprint, render_template, redirect, url_for, flash, session, request
from model import AdminStaffData, GeneralQuotation , db

admin_view_general_quotation_bp = Blueprint('admin_view_general_quotation', __name__)

@admin_view_general_quotation_bp.route('/admin_view_general_quotation')
def admin_view_general_quotation():
    if 'user_id' not in session:
        flash('Oops! Looks like you need a VIP pass to enter this area. Admins and Staff only, please!', 'info')
        return redirect(url_for('login.login'))
    
    if 'role' not in session or session['role'] not in ['Admin', 'Staff']:
        flash('Ah, ah, ah! You need to be an admin or staff to access this page. No sneak peeks allowed!', 'failed')
        return redirect(url_for('login.login'))
    
    user_id = session['user_id']
    user = AdminStaffData.query.get(user_id)
    
    if not user or user.role not in ['Admin', 'Staff']:
        flash('Ah, ah, ah! You need to be an admin or staff to access this page. No sneak peeks allowed!', 'failed')
        return redirect(url_for('login.login'))
    
    # Pagination
    page = request.args.get('page', 1, type=int)
    per_page = 10
    quotations = GeneralQuotation.query.paginate(page=page, per_page=per_page)
    
    return render_template('admin_view_general_quotation.html', quotations=quotations)


@admin_view_general_quotation_bp.route('/update_status', methods=['POST'])
def update_status():
    if 'user_id' not in session:
        flash('Oops! Looks like you need a VIP pass to enter this area. Admins and Staff only, please!', 'info')
        return redirect(url_for('login.login'))
    
    if 'role' not in session or session['role'] not in ['Admin', 'Staff']:
        flash('Ah, ah, ah! You need to be an admin or staff to access this page. No sneak peeks allowed!', 'failed')
        return redirect(url_for('login.login'))
    
    user_id = session['user_id']
    user = AdminStaffData.query.get(user_id)
    
    if not user or user.role not in ['Admin', 'Staff']:
        flash('Ah, ah, ah! You need to be an admin or staff to access this page. No sneak peeks allowed!', 'failed')
        return redirect(url_for('login.login'))
    
    quotation_id = request.form.get('quotation_id')
    status = request.form.get('status')

    quotation = GeneralQuotation.query.get(quotation_id)
    if not quotation:
        flash('Quotation not found.', 'failed')
        return redirect(request.referrer or url_for('admin_view_general_quotation.admin_view_general_quotation'))
    
    quotation.status = status
    try:
        db.session.commit()
        flash('Status updated successfully.', 'success')
    except Exception as e:
        flash('An error occurred while updating the status.', 'failed')
        db.session.rollback()
    
    return redirect(url_for('admin_view_general_quotation.admin_view_general_quotation'))



@admin_view_general_quotation_bp.route('/delete_quotation/<int:quotation_id>', methods=['GET', 'POST'])
def delete_quotation(quotation_id):
    if 'user_id' not in session:
        flash('Oops! Looks like you need a VIP pass to enter this area. Admins and Staff only, please!', 'info')
        return redirect(url_for('login.login'))
    
    if 'role' not in session or session['role'] not in ['Admin', 'Staff']:
        flash('Ah, ah, ah! You need to be an admin or staff to access this page. No sneak peeks allowed!', 'failed')
        return redirect(url_for('login.login'))
    
    user_id = session['user_id']
    user = AdminStaffData.query.get(user_id)
    
    if not user or user.role not in ['Admin', 'Staff']:
        flash('Ah, ah, ah! You need to be an admin or staff to access this page. No sneak peeks allowed!', 'failed')
        return redirect(url_for('login.login'))
    
    quotation = GeneralQuotation.query.get(quotation_id)
    if not quotation:
        flash('Quotation not found.', 'failed')
        return redirect(url_for('admin_view_general_quotation.admin_view_general_quotation'))
    
    try:
        db.session.delete(quotation)
        db.session.commit()
        flash('Quotation deleted successfully.', 'success')
    except Exception as e:
        flash('An error occurred while deleting the quotation.', 'failed')
        db.session.rollback()
    
    return redirect(url_for('admin_view_general_quotation.admin_view_general_quotation'))
