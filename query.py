"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
brand_8 = Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
chevy_corvette_models = Model.query.filter_by(name = 'Corvette', brand_name = 'Chevrolet').all()

# Get all models that are older than 1960.
sixties_plus_models = Model.query.filter(Model.year > 1960).all()

# Get all brands that were founded after 1920.
post_twenty_brands = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
cor_models = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
living_brands_1903 = Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
discontinued_or_neolithic = Brand.query.filter( (Brand.discontinued != None) | (Brand.founded < 1950) ).all()

# Get all models whose brand_name is not Chevrolet.
not_chevy = Model.query.filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    years_models = db.session.query(Model.name, Model.brand_name, Brand.headquarters).join(Brand).filter(Model.year == year).all()
    
    if years_models:
        for model in years_models:
            print "model: {}, brand name: {}, brand headquarters: {}".format(*model)

    # # alternatively, could do a joined load:

    # years_models = Model.query.options(db.joinedload('brand')).filter(Model.year == year).all()

    # if years_models:
    #     for model in years_models:
    #         print "{} {} {}".format(model.name, model.brand_name, model.brand.headquarters)

    else:
        print "no models were made that year"



def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brands = db.session.query(Brand).outerjoin(Model).all()

    for brand in brands:
        print brand.name + ":"
        # use set comprehension to eliminate duplicate model names, e.g. if a brand has multiple models with the same name from different years 
        for name in {model.name for model in brand.models}:
            print "\t" + name

    # # or use a joined load: 

    # brands = Brand.query.options(db.joinedload('models')).all()

    # for brand in brands:
    #     print brand.name + ":"
    #     # use set comprehension to eliminate duplicate model names, e.g. if a brand has multiple models with the same name from different years 
    #     for name in {model.name for model in brand.models}:
    #         print "\t" + name


# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(name='Ford')``?
"""
The datatype is an object called flask_sqlalchemy.BaseQuery, so it is an instance of the BaseQuery class defined in Flask SQLAlchemy. The value is <flask_sqlalchemy.BaseQuery at 0x7fbbf1360190>, so that just means it is an instance of the BaseQuery class located at that location in memory. 

Because we pass in db.Model as an argument when we create the Brand class in model.py, we are inheriting a bunch of methods that the creators of Flask SQLAlchemy defined on the Flask SQLAlchemy Model class. 'query' is one of those methods, and when we call it on an instance of our car Brand class (we instantiate an instance of the Brand class in the first part of the expression), it returns a BaseQuery object, an instance of the BaseQuery class, which we can then use to ask for information from our car Brand table. 'filter_by' is an instance method we inherit from the BaseQuery class or one of its parents, so now that we have a BaseQuery instance (which we got by calling Brand.query), we can call 'filter_by' on that instance to add additional specifications to our search.

Then, when we call something like 'all' or 'first' on the BaseQuery instance, both of which are also just instance methods defined in the BaseQuery class or one of its parents, those methods actually execute the query and return the results from the database. In this case, it would return a list of Brand objects that have the instance attribute name == 'Ford' (in other words, a list of one object, the brand Ford).

In short, the BaseQuery object allows us to query the database we've connected to.
"""
# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?
"""
An association table is the 'glue' between two tables that have a many to many relationship. It has no meaningful fields of its own, but rather exists only to connect the other two tables. In SQLAlchemy, it can be useful to create an association table so that you can directly reference the related rows/instances of either of the tables from a row/instance of the other table. 

For example, if you have a book table and a genre table, each book can be associated with many genres, and each genre associated with many books. If you create a bookgenre association table, and then create a relationship between the book and genre tables by saying that they have a secondary relationship, connected through the bookgenre table (which has no additional information other than the bookgenre id (pk for bookgenre table), the book id (pk for book table), and the genre id (pk for genre table)), then when you have a book instance, you can access all its related genre instances and vice versa, if you have a backref defined.

An association is different from middle tables, which do have meaningful fields of their own but can also be used to 'connect' many to many tables.
"""

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    """returns a list of brand objects whose brand name includes the string (case insensitive)"""

    return Brand.query.filter(Brand.name.ilike('%'+ mystr + '%')).all()


def get_models_between(start_year, end_year):
    """returns a list of model objects made between the inputted start year (inclusive) and end year (exclusive)"""

    return Model.query.filter(Model.year >= start_year, Model.year < end_year).all()
