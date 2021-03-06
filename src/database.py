from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Geneset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Integer, unique=True, nullable=False)
    scientific = db.Column(db.Text, unique=False, nullable=False)
    common = db.Column(db.Text, unique=False, nullable=False)
    dataset = db.Column(db.Text, unique=False, nullable=False)
    url = db.Column(db.Text, unique=False, nullable=False)

    def __init__(self, code, scientific, common, dataset, url):
        self.code = code
        self.scientific = scientific
        self.common = common
        self.dataset = dataset
        self.url = url

    def json(self):
        return {
            'download.code': self.code,
            'sp.scientific': self.scientific,
            'sp.common': self.common,
            'dataset': self.dataset,
            'url': self.url
        }

    @classmethod
    def find_by_code(cls, code):
        return cls.query.filter_by(code=code).first()

    def save_to(self):
        db.session.add(self)
        db.session.commit()

    def delete_(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def delete_all(cls):
        [item.delete_() for item in cls.query.all()]
        db.session.commit()


class Dataset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Integer, unique=True, nullable=False)
    scientific = db.Column(db.Text, unique=False, nullable=False)
    common = db.Column(db.Text, unique=False, nullable=False)
    layer = db.Column(db.Text, unique=False, nullable=False)
    protocol = db.Column(db.Text, unique=False, nullable=False)
    identity = db.Column(db.Text, unique=False, nullable=False)
    genes = db.Column(db.Integer, unique=False, nullable=False)
    cells = db.Column(db.Integer, unique=False, nullable=False)
    authors = db.Column(db.Text, unique=False, nullable=False)
    doi = db.Column(db.Text, unique=False, nullable=False)
    raw = db.Column(db.Text, unique=False, nullable=False)

    def __init__(self, code, scientific, common, layer, protocol, identity, genes, cells, authors, doi, raw):
        self.code = code
        self.scientific = scientific
        self.common = common
        self.layer = layer
        self.protocol = protocol
        self.identity = identity
        self.genes = genes
        self.cells = cells
        self.authors = authors
        self.doi = doi
        self.raw = raw

    def json(self):
        return {
            'download.code': self.code,
            'sp.scientific': self.scientific,
            'sp.common': self.common,
            'bio.layer': self.layer,
            'seq.protocol': self.protocol,
            'cell.identity': self.identity,
            'n.genes': self.genes,
            'n.cells': self.cells,
            'ref.authors': self.authors,
            'ref.doi': self.doi,
            'raw.dataset': self.raw
        }

    @classmethod
    def find_by_code(cls, code):
        return cls.query.filter_by(code=code).first()

    def save_to(self):
        db.session.add(self)
        db.session.commit()

    def delete_(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def delete_all(cls):
        [item.delete_() for item in cls.query.all()]
        db.session.commit()


class Graph(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Integer, unique=True, nullable=False)
    scientific = db.Column(db.Text, unique=False, nullable=False)
    common = db.Column(db.Text, unique=False, nullable=False)
    dataset = db.Column(db.Integer, unique=False, nullable=False)
    layer = db.Column(db.Text, unique=False, nullable=False)
    identity = db.Column(db.Text, unique=False, nullable=False)
    algorithm = db.Column(db.Text, unique=False, nullable=False)
    arguments = db.Column(db.Text, unique=False, nullable=False)
    nodes = db.Column(db.Integer, unique=False, nullable=False)
    edges = db.Column(db.Integer, unique=False, nullable=False)
    undirected = db.Column(db.Integer, unique=False, nullable=False)
    directed = db.Column(db.Integer, unique=False, nullable=False)
    url = db.Column(db.Text, unique=False, nullable=False)

    def __init__(self, code, scientific, common, dataset, layer, identity, algorithm, arguments, nodes, edges, undirected, directed, url):
        self.code = code
        self.scientific = scientific
        self.common = common
        self.dataset = dataset
        self.layer = layer
        self.identity = identity
        self.algorithm = algorithm
        self.arguments = arguments
        self.nodes = nodes
        self.edges = edges
        self.undirected = undirected
        self.directed = directed
        self.url = url

    def json(self):
        return {
            'download.code': self.code,
            'sp.scientific': self.scientific,
            'sp.common': self.common,
            'dataset': self.dataset,
            'bio.layer': self.layer,
            'cell.identity': self.identity,
            'algorithm': self.algorithm,
            'algorithm.args': self.arguments,
            'n.nodes': self.nodes,
            'n.edges': self.edges,
            'n.undirected.edges': self.undirected,
            'n.directed.edges': self.directed,
            'url': self.url
        }

    @classmethod
    def find_by_code(cls, code):
        return cls.query.filter_by(code=code).first()

    def save_to(self):
        db.session.add(self)
        db.session.commit()

    def delete_(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def delete_all(cls):
        [item.delete_() for item in cls.query.all()]
        db.session.commit()
