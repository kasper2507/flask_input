from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class UdlaanForm(FlaskForm):
    customerID = StringField('Customer ID')
    inventoryID = StringField('Inventory ID')
    staffID = StringField('Staff ID')
    amount = StringField('amount')
    submit = SubmitField('Submit')
