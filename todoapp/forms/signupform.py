from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length

class SignupForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(message="Username is invalid"), 
                                                   Length(min=4, max=15, message="Username must have between 4 and 15 characters")], 
                           render_kw={"placeholder":"Username"})
    
    password = PasswordField('password', validators=[InputRequired(message="Password is invalid"), 
                                                     Length(min=4, max=80, message="Password must have between 4 and 80 characters")], 
                             render_kw={"placeholder":"Password"})