from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

VERSION = '1'
DESCRIPTION = '"The Cat Api" api wrapper in python.'
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
  install_requires=['requests'],
)
