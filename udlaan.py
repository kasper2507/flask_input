from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class UdlaanForm(FlaskForm):
    customerID = StringField('Kunde ID')
    submit = SubmitField('Register')
"""
inventoryID = StringField('')
staffID = StringField('Staff ID')
amount = StringField('amount')
"""