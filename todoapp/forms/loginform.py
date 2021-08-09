from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import InputRequired, Length

class LoginForm(FlaskForm):
    username = StringField(label='username', validators=[InputRequired(message="username invalid"), 
                                                         Length(min=4, max=15, message="Username must have between 4 and 15 characters")], 
                           render_kw={"placeholder":"Username"})
    
    password = PasswordField(label='password', validators=[InputRequired(message="password invalid"), 
                                                           Length(min=4, max=80, message="Password must have between 4 and 80 characters")], 
                             render_kw={"placeholder":"Password"})
    
    remember = BooleanField(label='remember me')