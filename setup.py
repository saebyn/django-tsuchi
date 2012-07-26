"""
distutils setup.py file.

"""

from distutils.core import setup

setup(
    name = 'django-tsuchi',
    version = '0.0.1',
    description = 'Immediate notifications for users on Django-based sites.',

    long_description = open('README.rst').read(),
    packages = ['django_tsuchi'],

    maintainer = 'John Weaver',
    maintainer_email = 'john@saebyn.info',
)
