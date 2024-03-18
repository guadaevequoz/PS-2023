from src.core.database import db


class Institucion(db.Model):
    __tablename__ = "institucion"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    nombre = db.Column(db.String, nullable=False, unique=True)
    info = db.Column(db.String, nullable=False)
    direccion = db.Column(db.String, nullable=False)
    web = db.Column(db.String, nullable=False)
    palabra_clave = db.Column(db.ARRAY(db.String), nullable=False)
    horario_atencion = db.Column(db.String, nullable=False)
    habilitado = db.Column(db.Boolean, nullable=False)
    telefono = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    latitud = db.Column(db.Float)
    longitud = db.Column(db.Float)

    def __init__(
        self,
        nombre=None,
        info=None,
        direccion=None,
        web=None,
        palabra_clave=None,
        horario_atencion=None,
        email=None,
        telefono=None,
        latitud=None,
        longitud=None
    ):
        self.nombre = nombre
        self.info = info
        self.direccion = direccion
        self.web = web
        self.palabra_clave = palabra_clave
        self.horario_atencion = horario_atencion
        self.habilitado = False
        self.email = email
        self.telefono = telefono
        self.latitud = latitud
        self.longitud=longitud
