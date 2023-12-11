from app import app, db, Usuario
from werkzeug.security import generate_password_hash

def init_db():
    with app.app_context():
        Usuario.query.delete()
        usuario1 = Usuario(usuario='Ricardo', contraseña=generate_password_hash('12345'), rol='admin')
        usuario2 = Usuario(usuario='Gabo', contraseña=generate_password_hash('1234'))
        usuario3 = Usuario(usuario='Ivonne', contraseña=generate_password_hash('123'))
        usuario4 = Usuario(usuario='Xime', contraseña=generate_password_hash('2310'))



        db.session.add(usuario1)
        db.session.add(usuario2)
        db.session.add(usuario3)
        db.session.add(usuario4)


        # Confirmar los cambios
        db.session.commit()

        # Imprimir los usuarios y contraseñas
        print("Usuarios creados:")
        print("Usuario: Ricardo, Contraseña: 12345")
        print("Usuario: Gabo, Contraseña: 1234")
        print("Usuario: Ivonne, Contraseña: 123")
        print("Usuario: Xime, Contraseña: 2310")

if __name__ == "__main__":
    init_db()


