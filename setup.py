"""
GitRemote

A simple tool to add git remotes effortlessly

1. pip install gitremote
2. gitremote -i | gitremote --init
    It will create gitremote.yml
    Add remote and host
3. gitremote -r | gitremote --reset

That's it
"""

from setuptools import setup
import gitremote

PACKAGE = gitremote

setup(
    name=PACKAGE.__NAME__,
    version=PACKAGE.__version__,
    license="MIT",
    author="Mardix",
    author_email="mardix@pylot.io",
    description="Simple tool to add git remotes effortlessly",
    long_description=__doc__,
    url='http://github.com/mardix/gitremote/',
    download_url='http://github.com/mardix/gitremote/tarball/master',
    py_modules=['gitremote'],
    entry_points=dict(console_scripts=['gitremote=gitremote:cli']),
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
