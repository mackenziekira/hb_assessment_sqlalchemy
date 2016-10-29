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
discontinued_or_neolithic = Brand.query.filter((Brand.discontinued != None) | (Brand.founded < 1950)).all()

# Get all models whose brand_name is not Chevrolet.
not_chevy = Model.query.filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    years_models = Model.query.filter_by(year = year).all()
    
    if years_models:
        for model in years_models:
            print "model: {}, brand name: {}, brand headquarters: {}".format(model.name, model.brand_name, model.brand.headquarters)
    else:
        print "no models were made that year"


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brands = Brand.query.all()

    for brand in brands:
        print brand.name + ":"
        # use set comprehension to eliminate duplicate model names, e.g. if a brand has multiple models with the same name from different years 
        for name in {model.name for model in brand.models}:
            print "\t" + name


# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(name='Ford')``?

# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass
