from flask import  render_template
from model import db,app


# Import and register blueprints after db initialization
from views.general_register import register_bp
from views.login import login_bp
from views.logout import logout_bp
from views.dashboard import dashboard_bp
from views.admin_dashboard import admin_dashboard_bp
from views.admin_create_staff import create_staff_bp
from views.staff_dashboard import staff_dashboard_bp
from views.general_quotation import general_quotation_bp
from views.admin_view_general_quotation import admin_view_general_quotation_bp
from views.admin_quotation_template import admin_quotation_template_bp

# Register blueprints

app.register_blueprint(register_bp)
app.register_blueprint(login_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(admin_dashboard_bp)
app.register_blueprint(create_staff_bp)
app.register_blueprint(staff_dashboard_bp)
app.register_blueprint(general_quotation_bp)
app.register_blueprint(admin_view_general_quotation_bp)
app.register_blueprint(admin_quotation_template_bp)

# Index page and other routes...
@app.route("/")
def home(): 
    return render_template("index.html")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
