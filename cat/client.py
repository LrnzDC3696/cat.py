import asyncio
import aiohttp
from .models import Cat

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
    self._session = None
  
  async def close(self):
    """
    Closes the session
    """
    session = self._session
    if session is not None:
      self._session = None
      await session.close()
  
  async def _get(self, path, params = None):
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
    if self._session is None:
      self._session = aiohttp.ClientSession()
    data = await self._session.get(CAT_URL + path, params=params or {}, headers={'x-api-key':self.api_key})
    return await data.json()
    
  async def get_cat(self,limit=0,page=0,order='rand'):
    """
    Gets all the cat object based on the parameters
    
    Parameters
    ----------
    limit : `int`, optional
      Limit of cat objects to return.
    page  : `int`, optional
      The results page to return. Pagination wouldn't work if order is not set.
    order : `str`
      The order in which the results are sorted by.
      rand for randomised, desc for descending order,
      and asc if ascending.
    
    Returns
    ----------
    list
      A list of cat objects
    """
    if order not in {'rand','desc','asc'}:
      raise ValueError('image_type must be rand, desc or asc')
    
    data = await self._get('/images/search',
      {"limit":limit,'page':page,'order':order}
    )
    return [Cat(cat_dict) for cat_dict in data]
  
  async def get_cat_breed(self, name, limit = 0, page = 0, order = 'rand'):
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
    if order not in {'rand','desc','asc', None}:
      raise ValueError('image_type must be rand, desc or asc')
    
    data = await self._get('/images/search', {'breeds':name, "limit":limit,'page':page,'order':order})
    return [Cat(cat_dict) for cat_dict in data]
  
  async def get_cat_category(self, category_ids, limit = 0, page = 0, order = 'rand'):
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
    if order not in {'rand','desc','asc', None}:
      raise ValueError('image_type must be rand, desc or asc')
    
    data = await self._get('/images/search', {'category_ids':category_ids, "limit":limit,'page':page,'order':order})
    return [Cat(cat_dict) for cat_dict in data]
  
  async def get_cat_image_type(self, image_type, limit = 0, page = 0, order = 'rand'):
    """
    Gets all the cat object based on the parameters
    
    Parameters
    ----------
    image_type : `str`
      Type of the image. Must be in jpg, png or gif
    
    Returns
    ----------
    list
      A list of cat objects
    """
    
    if image_type not in {'jpg','png','gif', None}:
      raise ValueError('image_type must be jpg, png or gif')
    
    data = await self._get('/images/search',
      {'mime_types':image_type, "limit":limit,'page':page,'order':order}
    )
    return [Cat(cat_dict) for cat_dict in data]
