try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Leonie Panzer',
    'url': 'URL to get it at.',
    'download url': 'Where to download it.',
    'author_email': 'leo_panzer14@yahoo.de',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'ex48'
}

setup(**config)
