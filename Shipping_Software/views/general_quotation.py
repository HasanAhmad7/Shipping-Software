from typing import Container
from flask import Blueprint, app, flash, redirect, render_template, request, session, url_for
from model import GeneralUser, AdminStaffData, GeneralQuotation, db

general_quotation_bp = Blueprint('general_quotation', __name__)

def validate_numeric_input(value):
    try:
        return int(value)
    except ValueError:
        flash('Invalid input for numerical field.', 'error')
        return None

@general_quotation_bp.route('/general_quotation', methods=['GET', 'POST'])
def general_quotation():
    if 'user_id' not in session:
        flash('Hold your horses! You need to log in first to see this page.', 'info')
        return redirect(url_for('login.login'))
    
    
    user_id = session['user_id']
    user = GeneralUser.query.get(user_id)
    admin_staff_user = AdminStaffData.query.get(user_id)
    
    if user is None and admin_staff_user is None:
        flash('User not found. Please log in again.', 'error')
        return redirect(url_for('login.login'))

    return render_template('general_quotation.html')
        

@general_quotation_bp.route('/general_quotation_LCL', methods=['POST'])
def general_quotation_LCL():


    user_id = session['user_id']
    user = GeneralUser.query.get(user_id)
    admin_staff_user = AdminStaffData.query.get(user_id)

    if user:
        username = user.username
    elif admin_staff_user:
        username = admin_staff_user.username

    port_of_receipt = request.form['port_of_receipt']
    port_of_loading = request.form['port_of_loading']
    port_of_discharge = request.form['port_of_discharge']
    final_place_of_delivery = request.form['final_place_of_delivery']
    commodity_type = 'Hazardous' if request.form.get('commodity_type') else 'Non-hazardous'
    un_number = request.form['un_number']
    haz_class = request.form['haz_class']
    commodity = request.form['commodity']
    gross_weight = request.form['gross_weight']
    cbm = request.form['cbm']
    number_of_packages = request.form['number_of_packages']
    remark = request.form['remark']
    
    new_quotation = GeneralQuotation(
        shippment_type='LCL',
        port_of_receipt=port_of_receipt,
        port_of_loading=port_of_loading,
        port_of_discharge=port_of_discharge,
        final_place_of_delivery=final_place_of_delivery,
        commodity_type=commodity_type,
        un_number=un_number,
        haz_class=haz_class,
        commodity=commodity,
        gross_weight=gross_weight,
        cbm=cbm,
        number_of_packages=number_of_packages,
        remark=remark,
        status='Pending',
        created_by=username,
    )

    db.session.add(new_quotation)
    db.session.commit()
    
    flash('Quotation was created successfully.', 'success')
    return redirect(url_for('general_quotation.general_quotation'))


@general_quotation_bp.route('/general_quotation_FCL', methods=['POST'])
def general_quotation_FCL():
    user_id = session['user_id']
    user = GeneralUser.query.get(user_id)
    admin_staff_user = AdminStaffData.query.get(user_id)

    if user:
        username = user.username
    elif admin_staff_user:
        username = admin_staff_user.username

    port_of_receipt = request.form['port_of_receipt']
    port_of_loading = request.form['port_of_loading']
    port_of_discharge = request.form['port_of_discharge']
    final_place_of_delivery = request.form['final_place_of_delivery']
    commodity_type = 'Hazardous' if 'commodity_type' in request.form else 'Non-hazardous'
    un_number = request.form.get('un_number')
    haz_class = request.form.get('haz_class')
    container_type = request.form['container_type']
    number_of_containers = request.form['number_of_containers']
    commodity = request.form['commodity']
    gross_weight = request.form['gross_weight']
    remark = request.form['remark']

    new_quotation = GeneralQuotation(
        shippment_type='FCL',
        port_of_receipt=port_of_receipt,
        port_of_loading=port_of_loading,
        port_of_discharge=port_of_discharge,
        final_place_of_delivery=final_place_of_delivery,
        commodity_type=commodity_type,
        un_number=un_number,
        haz_class=haz_class,
        container_type=container_type,
        number_of_containers=number_of_containers,
        commodity=commodity,
        gross_weight=gross_weight,
        remark=remark,
        status='Pending',
        created_by=username
    )

    db.session.add(new_quotation)
    db.session.commit()


    flash('Quotation was created successfully.', 'success')
    return redirect(url_for('general_quotation.general_quotation'))

@general_quotation_bp.route('/general_quotation_BB', methods=['POST'])
def general_quotation_BB():
    user_id = session['user_id']
    user = GeneralUser.query.get(user_id)
    admin_staff_user = AdminStaffData.query.get(user_id)

    if user:
        username = user.username
    elif admin_staff_user:
        username = admin_staff_user.username

    port_of_receipt = request.form['port_of_receipt']
    port_of_loading = request.form['port_of_loading']
    port_of_discharge = request.form['port_of_discharge']
    final_place_of_delivery = request.form['final_place_of_delivery']
    commodity_type = 'Hazardous' if request.form.get('commodity_type') else 'Non-hazardous'
    un_number = request.form.get('un_number')
    haz_class = request.form.get('haz_class')
    type_of_vessel = request.form['type_of_vessel']
    commodity = request.form['commodity']
    gross_weight = request.form['gross_weight']
    remark = request.form['remark']

    new_quotation = GeneralQuotation(
        shippment_type='BB',
        port_of_receipt=port_of_receipt,
        port_of_loading=port_of_loading,
        port_of_discharge=port_of_discharge,
        final_place_of_delivery=final_place_of_delivery,
        commodity_type=commodity_type,
        un_number=un_number,
        haz_class=haz_class,
        type_of_vessel=type_of_vessel,
        commodity=commodity,
        gross_weight=gross_weight,
        remark=remark,
        status='Pending',
        created_by=username
    )

    db.session.add(new_quotation)
    db.session.commit()

    flash('Quotation was created successfully.', 'success')
    return redirect(url_for('general_quotation.general_quotation'))


@general_quotation_bp.route('/general_quotation_AIR', methods=['POST'])
def general_quotation_AIR():
    user_id = session['user_id']
    user = GeneralUser.query.get(user_id)
    admin_staff_user = AdminStaffData.query.get(user_id)

    if user:
        username = user.username
    elif admin_staff_user:
        username = admin_staff_user.username

    port_of_receipt = request.form['port_of_receipt']
    port_of_loading = request.form['port_of_loading']
    port_of_discharge = request.form['port_of_discharge']
    final_place_of_delivery = request.form['final_place_of_delivery']
    commodity_type = 'Hazardous' if request.form.get('commodity_type') else 'Non-hazardous'
    un_number = request.form.get('un_number')
    haz_class = request.form.get('haz_class')
    commodity = request.form['commodity']
    gross_weight = request.form['gross_weight']
    cbm = request.form['cbm']
    number_of_packages = request.form['number_of_packages']
    remark = request.form['remark']

    new_quotation = GeneralQuotation(
        shippment_type='Air',
        port_of_receipt=port_of_receipt,
        port_of_loading=port_of_loading,
        port_of_discharge=port_of_discharge,
        final_place_of_delivery=final_place_of_delivery,
        commodity_type=commodity_type,
        un_number=un_number,
        haz_class=haz_class,
        commodity=commodity,
        gross_weight=gross_weight,
        cbm=cbm,
        number_of_packages=number_of_packages,
        remark=remark,
        status='Pending',
        created_by=username
    )

    db.session.add(new_quotation)
    db.session.commit()

    flash('Quotation was created successfully.', 'success')
    return redirect(url_for('general_quotation.general_quotation'))




if __name__ == '__main__':
    app.run(debug=True)
    

