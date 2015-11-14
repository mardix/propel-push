"""
propel-push

extension that allows you to push to
git remotes specified in `propel.yml`, which is also the config file to deploy with Propel.

"""

from setuptools import setup
import propel_push

PACKAGE = propel_push

setup(
    name=PACKAGE.__NAME__,
    version=PACKAGE.__version__,
    license="MIT",
    author="Mardix",
    author_email="mardix@pylot.io",
    description=__doc__,
    long_description=__doc__,
    url='http://github.com/mardix/propel-push/',
    download_url='http://github.com/mardix/propel-push/tarball/master',
    py_modules=['propel_push'],
    entry_points=dict(console_scripts=['propel-push=propel_push:cli']),
    keywords=['git remote'],
    platforms='any',
    install_requires=['pyyaml==3.11'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    zip_safe=False
)
