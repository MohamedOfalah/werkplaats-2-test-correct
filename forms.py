from db_data import *
from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField, SubmitField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class vraagForm(FlaskForm):
    db_connection = connect_to_database("testcorrect_vragen.db")
    leerdoelen = get_db_data(
        db_connection, f"SELECT * FROM leerdoelen").fetchall()

    leerdoel = SelectField(u'Leerdoel', validators=[DataRequired()], choices=[(leerdoel['id'], f"{leerdoel['id']} - {leerdoel['leerdoel']}") for leerdoel in leerdoelen])
    vraag = TextAreaField(validators=[DataRequired(), Length(min=1, max=500)])
    opslaan = SubmitField("Wijzigingen opslaan")


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField("username", validators=[
                                 DataRequired(), Length(min=2, max=20)])
    password = PasswordField("password", validators=[DataRequired()])
    submit = SubmitField("Log in")
