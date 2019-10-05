# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from .admin_model import Employee

class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
    username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder": "Username"})
    first_name = StringField('First Name', validators=[DataRequired()], render_kw={"placeholder": "First Name"})
    last_name = StringField('Last Name', validators=[DataRequired()], render_kw={"placeholder": "Last Name"})
    password = PasswordField('Password', validators=[
                                        DataRequired(),
                                        EqualTo('confirm_password')
                                        ], render_kw={"placeholder": "Password"})
    confirm_password = PasswordField('Confirm Password', render_kw={"placeholder": "Retype Password"})
    #submit = SubmitField('Register')

    def validate_email(self, field):
        if Employee.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

    def validate_username(self, field):
        if Employee.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use.')

class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Password"})
    #submit = SubmitField('Login')