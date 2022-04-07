from app import basededatos, Persona

# Añadir Personas
persona1 = Persona("Katherine", "katty@gmail.com", "hola1234")
persona2 = Persona("Myrella", "myrella@gmail.com", "hola1234")

basededatos.session.add_all([persona1, persona2])
basededatos.session.commit()

# Realizar consulta de toda la tabla
personas = Persona.query.all()
print(personas)