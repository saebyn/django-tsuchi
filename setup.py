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

    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
   ],

)
