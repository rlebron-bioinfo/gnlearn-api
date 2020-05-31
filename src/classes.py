from src.database import Geneset, Dataset, Graph
from src.password import hash_, verify_pwd
from flask_restful import Resource, reqparse
import csv

class Populate(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('password', type=str, required=True, help='Administrator Password')

    def post(self):
        args = Populate.parser.parse_args()
        if verify_pwd(args['password'], hash_):
            Geneset.delete_all()
            genesets = open('db/genes.tsv', 'rt')
            genesets.readline()
            genesets = csv.reader(genesets, delimiter='\t')
            for item in genesets:
                item[0] = int(item[0])
                item = Geneset(*item)
                item.save_to()
            Dataset.delete_all()
            datasets = open('db/datasets.tsv', 'rt')
            datasets.readline()
            datasets = csv.reader(datasets, delimiter='\t')
            for item in datasets:
                item[0] = int(item[0])
                item[6] = int(item[6])
                item[7] = int(item[7])
                item = Dataset(*item)
                item.save_to()
            Graph.delete_all()
            graphs = open('db/graphs.tsv', 'rt')
            graphs.readline()
            graphs = csv.reader(graphs, delimiter='\t')
            for item in graphs:
                item[0] = int(item[0])
                item[3] = int(item[3])
                item[8] = int(item[8])
                item[9] = int(item[9])
                item[10] = int(item[10])
                item[11] = int(item[11])
                item = Graph(*item)
                item.save_to()
            return {'Message': 'Database has been updated!'}
        else:
            return {'Message': 'Wrong password!'}

class All_Genesets(Resource):
    def get(self):
        return list(map(lambda item: item.json(), Geneset.query.all()))

class Geneset_Cls(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('password', type=str, required=True, help='Administrator Password')
    parser.add_argument('code', type=int, required=True, help='Download Code')
    parser.add_argument('scientific', type=str, required=True, help='Species (Scientific Name)')
    parser.add_argument('common', type=str, required=True, help='Species (Common Name)')
    parser.add_argument('dataset', type=str, required=True, help='Dataset Name')
    parser.add_argument('url', type=str, required=True, help='Dataset URL')

    def get(self, code):
        item = Geneset.find_by_code(code)
        if item:
            return item.json()
        return {'Message': 'Geneset was not found!'}

    def post(self, code):
        if Geneset.find_by_code(code):
            return {'Message': 'Geneset #{} already exists!'.format(code)}
        args = Geneset_Cls.parser.parse_args()
        if verify_pwd(args['password'], hash_):
            item = Geneset(args['code'],
                           args['scientific'],
                           args['common'],
                           args['dataset'],
                           args['url'])
            item.save_to()
            return item.json()
        else:
            return {'Message': 'Wrong password!'}

    def put(self, code):
        item = Geneset.find_by_code(code)
        args = Geneset_Cls.parser.parse_args()
        if verify_pwd(args['password'], hash_):
            item.scientific = args['scientific']
            item.common = args['common']
            item.dataset = args['dataset']
            item.url = args['url']
            item.save_to()
            return item.json()
        else:
            return {'Message': 'Wrong password!'}

    def delete(self, code):
        item = Geneset.find_by_code(code)
        args = Geneset_Cls.parser.parse_args()
        if item:
            item.delete_()
            return {'Message': 'Geneset #{} has been deleted!'.format(code)}
        return {'Message': 'Geneset #{} does not exist!'.format(code)}

class All_Datasets(Resource):
    def get(self):
        return list(map(lambda item: item.json(), Dataset.query.all()))

class Dataset_Cls(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('password', type=str, required=True, help='Administrator Password')
    parser.add_argument('code', type=int, required=True, help='Download Code')
    parser.add_argument('scientific', type=str, required=True, help='Species (Scientific Name)')
    parser.add_argument('common', type=str, required=True, help='Species (Common Name)')
    parser.add_argument('layer', type=str, required=True, help='Biological Information Layer')
    parser.add_argument('protocol', type=str, required=True, help='Sequencing Protocol')
    parser.add_argument('identity', type=str, required=True, help='Cell Identity')
    parser.add_argument('genes', type=int, required=True, help='Number of Genes')
    parser.add_argument('cells', type=int, required=True, help='Number of Cells')
    parser.add_argument('authors', type=str, required=True, help='Authors (Reference Publication)')
    parser.add_argument('doi', type=str, required=True, help='DOI (Reference Publication)')
    parser.add_argument('raw', type=str, required=True, help='Raw Dataset (URL)')

    def get(self, code):
        item = Dataset.find_by_code(code)
        if item:
            return item.json()
        return {'Message': 'Dataset was not found!'}

    def post(self, code):
        if Dataset.find_by_code(code):
            return {'Message': 'Dataset #{} already exists!'.format(code)}
        args = Dataset_Cls.parser.parse_args()
        if verify_pwd(args['password'], hash_):
            item = Dataset(args['code'],
                           args['scientific'],
                           args['common'],
                           args['layer'],
                           args['protocol'],
                           args['identity'],
                           args['genes'],
                           args['cells'],
                           args['authors'],
                           args['doi'],
                           args['raw'])
            item.save_to()
            return item.json()
        else:
            return {'Message': 'Wrong password!'}

    def put(self, code):
        item = Dataset.find_by_code(code)
        args = Dataset_Cls.parser.parse_args()
        if verify_pwd(args['password'], hash_):
            item.scientific = args['scientific']
            item.common = args['common']
            item.layer = args['layer']
            item.protocol = args['protocol']
            item.identity = args['identity']
            item.genes = args['genes']
            item.cells = args['cells']
            item.authors = args['authors']
            item.doi = args['doi']
            item.raw = args['raw']
            item.save_to()
            return item.json()
        else:
            return {'Message': 'Wrong password!'}

    def delete(self, code):
        item = Dataset.find_by_code(code)
        args = Dataset_Cls.parser.parse_args()
        if item:
            item.delete_()
            return {'Message': 'Dataset #{} has been deleted!'.format(code)}
        return {'Message': 'Dataset #{} does not exist!'.format(code)}

class All_Graphs(Resource):
    def get(self):
        return list(map(lambda item: item.json(), Graph.query.all()))

class Graph_Cls(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('password', type=str, required=True, help='Administrator Password')
    parser.add_argument('code', type=int, required=True, help='Download Code')
    parser.add_argument('scientific', type=str, required=True, help='Species (Scientific Name)')
    parser.add_argument('common', type=str, required=True, help='Species (Common Name)')
    parser.add_argument('dataset', type=int, required=True, help='Dataset Download Code')
    parser.add_argument('layer', type=str, required=True, help='Biological Information Layer')
    parser.add_argument('identity', type=str, required=True, help='Cell Identity')
    parser.add_argument('algorithm', type=str, required=True, help='Algorithm')
    parser.add_argument('arguments', type=str, required=True, help='Algorithm Arguments')
    parser.add_argument('nodes', type=int, required=True, help='Number of Nodes')
    parser.add_argument('edges', type=int, required=True, help='Number of Edges')
    parser.add_argument('undirected', type=int, required=True, help='Number of Undirected Edges')
    parser.add_argument('directed', type=int, required=True, help='Number of Directed Edges')
    parser.add_argument('url', type=str, required=True, help='Dataset URL')

    def get(self, code):
        item = Graph.find_by_code(code)
        if item:
            return item.json()
        return {'Message': 'Graph was not found!'}

    def post(self, code):
        if Graph.find_by_code(code):
            return {'Message': 'Graph #{} already exists!'.format(code)}
        args = Graph_Cls.parser.parse_args()
        if verify_pwd(args['password'], hash_):
            item = Graph(args['code'],
                         args['scientific'],
                         args['common'],
                         args['dataset'],
                         args['layer'],
                         args['identity'],
                         args['algorithm'],
                         args['arguments'],
                         args['nodes'],
                         args['edges'],
                         args['undirected'],
                         args['directed'],
                         args['url'])
            item.save_to()
            return item.json()
        else:
            return {'Message': 'Wrong password!'}

    def put(self, code):
        item = Graph.find_by_code(code)
        args = Graph_Cls.parser.parse_args()
        if verify_pwd(args['password'], hash_):
            item.scientific = args['scientific']
            item.common = args['common']
            item.dataset = args['dataset']
            item.layer = args['layer']
            item.identity = args['identity']
            item.algorithm = args['algorithm']
            item.arguments = args['arguments']
            item.nodes = args['nodes']
            item.edges = args['edges']
            item.undirected = args['undirected']
            item.directed = args['directed']
            item.url = args['url']
            item.save_to()
            return item.json()
        else:
            return {'Message': 'Wrong password!'}

    def delete(self, code):
        item = Graph.find_by_code(code)
        args = Graph_Cls.parser.parse_args()
        if item:
            item.delete_()
            return {'Message': 'Graph #{} has been deleted!'.format(code)}
        return {'Message': 'Graph #{} does not exist!'.format(code)}
