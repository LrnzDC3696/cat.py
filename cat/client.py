from requests import get
from urllib.parse import urljoin

from models import Cat

CAT_URL = 'https://api.thecatapi.com/v1'

class Client:
  
  def __init__(self, api_key = None):
    self.api_key = api_key
  
  def _get(self, path, params = {}):
    return get(CAT_URL + path, params=params, headers={'x-api-key':self.api_key}).json()

  def get_cat(self,limit=None,page=None,order='rand'):
    data = self._get('/images/search?',
      {"limit":limit,'page':page,'order':'desc' if order else 'asc'}
    )
    return [Cat(cat_dict) for cat_dict in data]
  
  def get_cat_breed(self, name=None):
    data = self._get('/images/search?', {'breeds':name})
    return [Cat(cat_dict) for cat_dict in data]
  
  def get_cat_category(self, category_ids):
    data = self._get('/images/search?', {'category_ids':category_ids})
    return [Cat(cat_dict) for cat_dict in data]
  
  def get_cat_image_type(self, image_type):
    data = self._get('/images/search?', {'mime_types':image_type})
    return [Cat(cat_dict) for cat_dict in data]
