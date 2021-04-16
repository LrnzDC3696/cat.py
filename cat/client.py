from requests import get
from models import Cat

CAT_URL = 'https://api.thecatapi.com/v1'

class Client:
  """
  Represents a client object.
  """
  
  def __init__(self, api_key):
    """
    Parameters
    ----------
    api_key : `str`
      Api key for your client.
    """
    self.api_key = api_key
  
  def _get(self, path, params = {}):
    """
    Requests data from the cat api.
    
    Parameters
    ----------
    path : `str`
      Path of course I think...
    
    Returns
    ----------
    dict
      A dictionary that contains all of the cat info needed.
    """
    return get(CAT_URL + path, params=params, headers={'x-api-key':self.api_key}).json()

  def get_cat(self,limit=None,page=None,order='rand'):
    """
    Gets all the cat object based on the parameters
    
    Parameters
    ----------
    limit : `int`, optional
      Limit of cat objects to return.
    page  : `int`, optional
      The results page to return. Pagination wouldn't work if order is not set.
    order : `bool`, default: None
      The order in which the results are sorted by.
      None for randomised, True if you want it in descending order,
      and False if ascending.
    
    Returns
    ----------
    list
      A list of cat objects
    """
    if order is None:
      order = 'rand'
    elif order:
      order = 'desc'
    else:
      order = 'asc'
    
    data = self._get('/images/search',
      {"limit":limit,'page':page,'order':order}
    )
    return [Cat(cat_dict) for cat_dict in data]
  
  def get_cat_breed(self, name):
    """
    Gets all the cat object based on the breed name
    
    Parameters
    ----------
    name : `str`
      The breeds' name.
    
    Returns
    ----------
    list
      A list of cat objects
    """
    data = self._get('/images/search', {'breeds':name})
    return [Cat(cat_dict) for cat_dict in data]
  
  def get_cat_category(self, category_ids):
    """
    Gets all the cat object based on the category
    
    Parameters
    ----------
    category_ids : `int`
      category id of cat objects to return.
    
    Returns
    ----------
    list
      A list of cat objects
    """
    data = self._get('/images/search', {'category_ids':category_ids})
    return [Cat(cat_dict) for cat_dict in data]
  
  def get_cat_image_type(self, image_type=None):
    """
    Gets all the cat object based on the parameters
    
    Parameters
    ----------
    image_type : `bool`, default: None
      None for jpg, True for gif, and False for png.
    
    Returns
    ----------
    list
      A list of cat objects
    """
    if image_type is None:
      image_type = 'jpg'
    elif image_type:
      image_type = 'gif'
    else:
      image_type = 'png'
    
    data = self._get('/images/search',
      {'mime_types':image_type}
    )
    return [Cat(cat_dict) for cat_dict in data]
