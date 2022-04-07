import os
from formulario import FormularioRegistro
from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config as cfg
from werkzeug.security import generate_password_hash, check_password_hash

directorio = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SECRET_KEY'] = cfg.secretkey
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{cfg.mysql["user"]}:{cfg.mysql["pass"]}@{cfg.mysql["host"]}/{cfg.mysql["db"]}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

basededatos = SQLAlchemy(app)
Migrate(app, basededatos)

class Persona(basededatos.Model):
    __tablename__ = 'Persona'
    id = basededatos.Column(basededatos.Integer, primary_key=True)
    nombre = basededatos.Column(basededatos.Text)
    correo = basededatos.Column(basededatos.Text)
    contrasena = basededatos.Column(basededatos.Text)

    def __init__(self, nombre, correo, contrasena):
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena

    def __repr__(self):
        texto = "\nPersona \nNombre: {} \nCorreo: {} \nContrasena: {}".format(self.nombre, self.correo, self.contrasena)
        return texto

@app.route('/')
def principal():
    return render_template('form.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    formulario = FormularioRegistro()
    if formulario.validate_on_submit():
        nombre = formulario.nombre.data
        correo = formulario.correo.data
        contrasena = formulario.contrasena.data
        contrasenaEncriptada = generate_password_hash(contrasena)
        persona = Persona(nombre,correo,contrasenaEncriptada)
        basededatos.session.add(persona)
        basededatos.session.commit()
        flash("Gracias {} por registrarse".format(nombre))
        return redirect(url_for('registro'))
    
    return render_template('form.html', formulario=formulario)

if __name__ == '__main__':
    app.run(debug=True)