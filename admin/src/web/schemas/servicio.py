from marshmallow import fields, Schema


class InstitucionSchema(Schema):
    nombre = fields.Str(required=True)
    info = fields.Str(required=True)
    direccion = fields.Str(required=True)
    web = fields.Str(required=True)
    horario_atencion = fields.Str(required=True)
    contacto = fields.Str(required=True)
    habilitado = fields.Bool(required=True)
    latitud=fields.Float(required=True)
    longitud=fields.Str(required=True)


class TipoSchema(Schema):
    nombre = fields.Str(required=True)


class ServicioSchema(Schema):
    id = fields.Str(required=True)
    nombre = fields.Str(required=True)
    descripcion = fields.Str(required=True)
    institucion = fields.Nested(InstitucionSchema())
    palabras_claves = fields.List(fields.String(), required=True)
    tipo = fields.Nested(TipoSchema())

class ServiciosPaginadosSchema(Schema):
    data = fields.Nested(ServicioSchema, many=True)
    page = fields.Int(required=True)
    per_page = fields.Int(required=True)
    total = fields.Int(required=True)


class TipoSchema(Schema):
    nombre = fields.Str(required=True)


class TiposServiciosSchema(Schema):
    data = fields.Nested(TipoSchema, many=True)


servicio_schema = ServicioSchema()
servicios_schema = ServicioSchema(many=True)
servicios_paginados_schema = ServiciosPaginadosSchema()
tipo_schema = TipoSchema(many=True)
tipos_servicios_schema = TiposServiciosSchema()
