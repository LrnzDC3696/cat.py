import re

cat_cache = {}

PARSE = re.compile('(\d+) *- *(\d+)')
def parse(text):
    return PARSE.fullmatch(text).groups()

class Breed:
  """
  A class representing a Breed object.
  
  Attributes
  ----------
  adaptability : `int`
    The adaptability level of the cat from 1-5.
  affection_level : `int`
    The affection level of the breed from 1-5. 
  alt_names : `list`
    A list of alternative names of the breed.
  cfa_url : `str`
    The cfa url for the breed.
  child_friendly : `int`
    The level of child friendliness of breed from 1-5.
  country_code : `str`
    The country code of the origin coutry of the breed.
  country_codes : `list`  
    A list of country codes where the breed exists.
  description : `str`
    The description of the breed containing details and such.
  dog_friendly : `int`
    The level of dog friendliness of the breed from 1-5.
  energy_level : `int`
    The energy level of the breed from 1-5.
  experimental : `bool`
    Whether the breed is experimental.
  grooming : `int`
    The grooming level of the breed from 1-5.
  hairless : `bool`
    Whether the breed is hairless or not.
  health_issues : `int`
    The level of health issues the breed has from 1-5.
  hypoallergenic : `bool`
    Whether the breed is hypoallergenic.
  id : `str`
    The id of the breed.
  indoor : `bool`
    Whether the breed naturaly lives indoor.
  intelligence : `int`
    The intelligence level of the breed from 1-5.
  life_span : `tuple`
    The life span of the breed.
  name : `str`
    The name of the breed.
  natural : `int`
    Whether the breed is natural or not.
  origin : `str`
    The origin country of the breed.
  rare : `bool`
    Whether the breed is rare.
  reference_image_id : `str`
    The reference image id of the breed.
  rex : `bool`
    Whether the breed is rex.
  shedding_level : `int`
    The shedding level of the breed.
  short_legs : `bool`
    Whether the breed has short legs.
  social_needs : `int`
    The social needs level of the breed from 1-5.
  stranger_friendly : `int`
    The stranger friendly level of the breed from 1-5.
  suppressed_tail : `bool`
    Whether the breed has a suppressed_tail.
  temperament : `list`
    A list of temperament of the breed.
  vcahospitals_url : `str`
    The vcahospitals url of the breed.
  vetstreet_url : `str`
    The vetstreet url of the breed.
  vocalisation : `int`
    The vocalisation level of the breed from 1-5.
  weight : `tuple`
    The metric weight of the breed.
  wikipedia_url : `str`
    The wikipedia url for the breed.
  """
  
  def __init__(self, breeds):
    """
    Parses the breeds dictionary and creates a new Breed object.
    
    Parameters
    ----------
    breeds : `dict`
      The source of all data.
    """
    self.adaptability = breeds.get('adaptability')
    self.affection_level = breeds.get('affection_level'
    
    alt_names = breeds.get('alt_names')
    self.alt_names = alt_names and alt_names.split(', ')
    
    self.cfa_url = breeds.get('cfa_url')
    self.child_friendly = breeds.get('child_friendly')
    self.country_code = breeds.get('country_code')
    
    codes = breeds.get('country_codes')
    self.country_codes = codes and codes.split(', ')
    
    self.description = breeds.get('description')
    self.dog_friendly = breeds.get('dog_friendly')
    self.energy_level = breeds.get('energy_level')
    self.experimental = bool(breeds.get('experimental']))
    self.grooming = breeds.get('grooming')
    self.hairless = bool(breeds.get('hairless'))
    self.health_issues = breeds.get('health_issues')
    self.hypoallergenic = bool(breeds.get('hypoallergenic'))
    self.id = breeds.get('id')
    self.indoor = bool(breeds.get('indoor'))
    self.intelligence = breeds.get('intelligence')
    
    life = breeds.get('life_span')
    self.life_span = life and parse(life)
    
    self.name = breeds.get('name')
    self.natural = bool(breeds.get('natural'))
    self.origin = breeds.get('origin')
    self.rare = bool(breeds.get('rare'))
    self.reference_image_id = breeds.get('reference_image_id')
    self.rex = bool(breeds.get('rex'))
    self.shedding_level = breeds.get('shedding_level')
    self.short_legs = bool(breeds.get('short_legs'))
    self.social_needs = breeds.get('social_needs')
    self.stranger_friendly = breeds.get('stranger_friendly')
    self.suppressed_tail = breeds.get('suppressed_tail')
    
    temperament = breeds.get('temperament')
    self.temperament = temperament or temperament.split(', ')
    
    self.vcahospitals_url = breeds.get('vcahospitals_url')
    self.vetstreet_url = breeds.get('vetstreet_url')
    self.vocalisation = breeds.get('vocalisation')
    
    weight = breeds.get('weight')
    metric = weight and weight.get('metric')
    self.weight = metric or parse(metric)
    self.wikipedia_url = breeds.get('wikipedia_url')
  
  def __repr__(self):
    """
    Returns the representation of the object.
    """
    return f"<{self.__class__.__name__} id={self.id!r}, name={self.name!r}>"

class Category:
  """
  A class to represent a Category object.
  
  Attributes
  ----------
  id : `int`
    The id of the category.
  name : `str`
    The name of the category.
  """
  
  def __init__(self, category):
    """
    Creates a new category object.
    
    Parameters
    ----------
    category : `dict`
      The source of data.
    """
    self.id = category['id']
    self.name = category['name']

  def __repr__(self):
    """
    Returns the representation of the object.
    """
    return f"<{self.__class__.__name__} id={self.id!r}, name={self.name!r}>"

class Cat:
  """
  A class representing a cat.
  
  Attributes
  ----------
  id : `str`
    The id of the cat image.
  url : `str`
    The url of the cat image.
  width : `int` 
    The width of the cat image.
  height : `int`
    The height of the cat image.
  breeds : `list`
    A list of breeds object.
  categories : `list`
    A list of category the cat is in.
  """
  
  def __new__(cls, data):
    """
    Creates a new Cat object if the object is not in cat_cache
    
    Parameters
    ----------
    data : `dict`
      The source of all data.
    """
    cat_id = data['id']
    try:
      return cat_cache[cat_id]
    except KeyError:
      pass
    
    self = object.__new__(cls)
    self.id = cat_id
    self.url = data['url']
    self.width = data['width']
    self.height = data['height']
    self.breeds = [Breed(breed_data) for breed_data in data['breeds']]
        
    try:
      category_datas = data['categories']
    except KeyError:
      categories = None
    else:
      categories = [Category(category_data) for category_data in category_datas]
    
    self.categories = categories    
    
    cat_cache[cat_id] = self
        
    return self
  
  def __repr__(self):
    """
    Returns the representation of the object.
    """
    return f"<{self.__class__.__name__} id={self.id!r}>"

#Not Implemented Yet
# class Favourite:
#  pass
#
#class ImageAnalysis:
#  pass
#
#class Sponsor:
#  pass
#
#class Vote:
#  pass
#
#class Source:
#  pass
#
#class Fact:
#  pass

