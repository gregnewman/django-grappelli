"""Django Grappelli

A nicer django admin skin.  this is a quick fix setup.py for my virtualenv
"""

from distutils.core import setup


description, long_description = __doc__.split('\n\n', 1)
VERSION = '0.2.1'

setup(
    name='grappelli',
    version=VERSION,
    author='sehmaschine',
    description=description,
    long_description=long_description,
    platforms=['any'],
    url='http://github.com/revyver/django-grappelli',
    download_url=("http://github.com/revyver/django-grappelli/tarball/a975573cc47677f4f65f75741027bccdc1dac9cf"),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        ],
    packages=[
        'django-grappelli',
        ],
    provides=['django-grappelli'],
    )
