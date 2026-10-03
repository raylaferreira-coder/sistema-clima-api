from flask import Flask
from flask_restful import Api
import os 
from dotenv import load_dotenv
from src.models.Base import db
from src.route.UsuarioEndpoints import initialize_usuario_endpoints
from src.route.EnderecoEndpoints import initialize_endereco_endpoints
from src.route.RegiaoEndpoints import initialize_regiao_endpoints
from src.route.MeteorologiaEndpoints import initialize_meteorologia_endpoints
from src.route.AuditoriaEndpoints import initialize_auditoria_endpoints

load_dotenv()

def create_app() -> Flask:
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    api = Api(app, prefix="/sistema_meteorologico")
    
    initialize_usuario_endpoints(api)
    initialize_endereco_endpoints(api)
    initialize_regiao_endpoints(api)
    initialize_meteorologia_endpoints(api)
    initialize_auditoria_endpoints(api)

    return app
    