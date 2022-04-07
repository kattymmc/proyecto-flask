from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired

class FormularioRegistro(FlaskForm):
    nombre = StringField('Nombre Completo', validators=[DataRequired()])
    correo = EmailField('Correo electrónico', validators=[DataRequired()])
    contrasena = PasswordField('Contraseña', validators=[DataRequired()])
    boton = SubmitField('Registrar')

