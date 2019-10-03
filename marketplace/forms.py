
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField, IntegerField, SelectField
from wtforms.validators import InputRequired, Length, Email, EqualTo, DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


#creates the login information
class LoginForm(FlaskForm):
    username = StringField("User Name", validators=[InputRequired('Enter user name')])
    password = PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

# this is the registration form
class RegisterForm(FlaskForm):
    username = StringField("User Name", validators=[InputRequired()])
    email = StringField("Email Address", validators=[Email("Please enter a valid email")])
    phone = StringField("Phone Number", validators=[DataRequired("Please enter a valid phone number")])

    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    #submit button
    submit = SubmitField("Register")


class CreateItemForm(FlaskForm):
    image = FileField('image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    name = StringField('Item Name', validators=[InputRequired()])
    description = TextAreaField('Item Description', validators=[InputRequired(), Length(min=10, max=200)])
    suburb = StringField('Suburb', validators=[InputRequired()])
    state = SelectField('State', validators=[InputRequired()], choices=[('QLD','QLD'),('NSW','NSW'),('ACT','ACT'), ('NT','NT'), ('WA','WA'), ('SA','SA'), ('TAS','TAS'), ('VIC','VIC')])
    category = SelectField('Category', validators=[InputRequired()], choices=[('Desktop','Desktop'),('Laptop','Laptop'),('All In One','All In One')])
    price = IntegerField('Price', validators=[InputRequired()])
    cpu = StringField('CPU', validators=[InputRequired()])
    ramgb = IntegerField('RAM (GB)', validators=[InputRequired()])
    totalgb = IntegerField('Total Storage (GB)', validators=[InputRequired()])
    submit = SubmitField("Create Listing")