from setuptools import setup, find_packages
import pathlib
import re


version_search_pattern = re.compile('^__version__[ ]*=[ ]*((?:\'[^\']+\')|(?:\"[^\"]+\"))[ ]*$', re.M)
parsed = version_search_pattern.search((HERE / 'hata' / '__init__.py').read_text())
if parsed is None:
    raise RuntimeError('No version found in `__init__.py`.')

VERSION = literal_eval(parsed.group(1))


here = pathlib.Path(__file__).parent.resolve()

DESCRIPTION = '"The Cat Api" async api wrapper in python.'
LONG_DESCRIPTION = (here / 'README.md').read_text(encoding='utf-8')


setup(
  name = 'cat.py',
  version = VERSION,
  description = DESCRIPTION,
  long_description = LONG_DESCRIPTION,
	long_description_content_type = 'text/markdown',
	url = 'https://github.com/WeMayNeverKnow/cat.py',
	author = 'WeMayNeverKnow',
	keywords = ['cats', 'api wrapper', 'thecatapi'],
  packages = find_packages(),
  install_requires=['aiohttp'],
)
