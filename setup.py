__author__ = 'karunab'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'FIFA Career Mode Players',
    'author': 'Karun Japhet',
    'url': '',
    'download_url': '',
    'author_email': 'karun@japhet.in',
    'version': '0.1',
    'install_requires': [],
    'packages': [''],
    'scripts': [],
    'name': 'fcmp'
}

setup(**config, requires=['BeautifulSoup', 'peewee', 'nose'])
