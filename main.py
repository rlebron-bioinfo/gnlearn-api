from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

from src.database import db
from src.classes import Populate, All_Genesets, Geneset_Cls, All_Datasets, Dataset_Cls

db.init_app(app)
app.app_context().push()
db.create_all()

api.add_resource(All_Genesets, '/genesets')
api.add_resource(Geneset_Cls, '/genesets/<int:code>')
api.add_resource(All_Datasets, '/datasets')
api.add_resource(Dataset_Cls, '/datasets/<int:code>')
api.add_resource(Populate, '/populate')

if __name__ == '__main__':
    app.run()
