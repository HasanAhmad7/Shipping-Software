import os
from flask import Blueprint, app, flash, redirect, render_template, request, session, url_for, Response
from model import GeneralQuotation, GeneralUser
import pdfkit
from bs4 import BeautifulSoup

admin_quotation_template_bp = Blueprint('admin_quotation_template', __name__)

@admin_quotation_template_bp.route('/admin_quotation_template/<int:quotation_id>', methods=['GET'])
def admin_quotation_template(quotation_id):
    if 'user_id' not in session:
        flash('Oops Looks like you need a VIP pass to enter this area. Admins and Staff only, please!', 'info')
        return redirect(url_for('login.login'))
    
    if 'role' not in session or session['role'] not in ['Admin', 'Staff']:
        flash('Ah, ah, ah You need to be an admin or staff to access this page. No sneak peeks allowed!', 'failed')
        return redirect(url_for('login.login'))

    quotation = GeneralQuotation.query.get(quotation_id)
    if not quotation:
        flash('Quotation not found.', 'failed')
        return redirect(url_for('admin_view_general_quotation.admin_view_general_quotation'))
    
    if quotation.status!= 'Completed':
        flash("Oh, you'd love to view the quotation? Sure, unfortunately the Quotation is still pending. No biggie, right? 😉", 'failed')
        return redirect(url_for('admin_view_general_quotation.admin_view_general_quotation'))
    
    customer = GeneralUser.query.filter_by(username=quotation.created_by).first()

    return render_template('admin_quotation_template.html', quotation=quotation, customer=customer)

wkhtmltopdf_path = "C:/Users/hasan/Desktop/Shipping_Software/wkhtmltopdf/bin/wkhtmltopdf.exe"
os.environ['WKHTMLTOPDF_PATH'] = wkhtmltopdf_path


def generate_pdf_from_html(main_content):
    pdf_data = pdfkit.from_string(main_content, False, options={'executablePath': wkhtmltopdf_path})
    return pdf_data


@admin_quotation_template_bp.route('/generate_pdf/<int:quotation_id>', methods=['get'])
def generate_pdf(quotation_id):
    quotation = GeneralQuotation.query.get(quotation_id)
    customer = GeneralUser.query.filter_by(username=quotation.created_by).first()

    if not quotation or not customer:
        return Response("Quotation or customer not found.", status=404)

    html_content = render_template('admin_quotation_template.html', quotation=quotation, customer=customer)
    soup = BeautifulSoup(html_content, 'html.parser')
    main_content = soup.find('div', id='main_content')
    if not main_content:
        return Response("Main content not found in HTML.", status=404)

    pdf_data = generate_pdf_from_html(str(main_content))

    return Response(pdf_data, mimetype='application/pdf', headers={'Content-Disposition': 'attachment; filename=quotation.pdf'})

if __name__ == '__main__':
    app.run(debug=True)
