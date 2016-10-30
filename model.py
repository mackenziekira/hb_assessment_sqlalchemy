"""Models and database functions for cars db."""

from flask_sqlalchemy import SQLAlchemy

# Here's where we create the idea of our database. We're getting this through
# the Flask-SQLAlchemy library. On db, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM

class Model(db.Model):
    """Car model."""

    __tablename__ = "models"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.Integer, nullable=False)
    brand_name = db.Column(db.String(50), db.ForeignKey('brands.name'))
    name = db.Column(db.String(50), nullable=False)

    brand = db.relationship('Brand', backref='models')

    def __repr__(self):
        """returns more readable info for model object"""

        return "name: {}, brand: {}, year: {}".format(self.name, self.brand_name, self.year)

    """Functions from query.py as class methods

    @classmethod
    def get_models_between(cls, start_year, end_year):
        '''returns a list of model objects made between the inputted start year (inclusive) and end year (exclusive)'''

        return cls.query.filter(cls.year >= start_year, cls.year < end_year).all()

    @classmethod
    def get_model_info(year):
        '''Takes in a year, and prints out each model, brand_name, and brand
        headquarters for that year using only ONE database query.'''

        years_models = db.session.query(Model.name, Model.brand_name, Brand.headquarters).join(Brand).filter(Model.year == year).all()
        
        if years_models:
            for model in years_models:
                print "model: {}, brand name: {}, brand headquarters: {}".format(*model)
        
        else:
            print "no models were made that year"
        """


class Brand(db.Model):
    """Car brand."""

    __tablename__ = "brands"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    founded = db.Column(db.Integer)
    headquarters = db.Column(db.String(50))
    discontinued = db.Column(db.Integer)

    def __repr__(self):
        """returns more readable info for brand object"""
        
        return "name: {}, founded: {}, discontinued: {}".format(self.name, self.founded, self.discontinued)

    """Functions from query.py as class methods
   
    @classmethod
    def search_brands_by_name(cls, mystr):
        '''returns a list of brand objects whose brand name includes the string (case insensitive)'''

        return cls.query.filter(cls.name.ilike('%'+ mystr + '%')).all()

    @classmethod
    def get_brands_summary():
        '''Prints out each brand name, and each model name for that brand
         using only ONE database query.'''

        brands = db.session.query(Brand).outerjoin(Model).all()

        for brand in brands:
            print brand.name + ":"
            # use set comprehension to eliminate duplicate model names, e.g. if a brand has multiple models with the same name from different years 
            for name in {model.name for model in brand.models}:
                print "\t" + name
    """

# End Part 1


##############################################################################
# Helper functions

def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///cars'
    # app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask

    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."
