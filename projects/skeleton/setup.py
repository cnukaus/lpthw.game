## Python 2

## Requirements:
## setuptools (built-in)
## If setuptools does not work, you must have:
## distribute from pypi.python.org/pypi/distribute (distutils)

try:
  from setuptools import setup
except:
  from distutils.core import setup
config={'description': 'MY_PROJECT', 'authour': 'Wensen Dong', 'url': 'https://github.com/real-python/lpthw.game/blob/master/projects/skeleton/setup.py?raw=true', 'download_url': 'https://github.com/real-python/lpthw.game/blob/master/projects/skeleton/setup.py?raw=true', 'authour_email': 'wensen.dong@education.nsw.gov.au', 'version': '0.1', 'install_requires': ['nose'], 'packages': ['NAME'], 'scripts': [], 'name': 'PROJECT_NAME'}
