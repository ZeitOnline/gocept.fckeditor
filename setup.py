from setuptools import setup

setup(
    name='gocept.fckeditor',
    version='2.6.4.1+importlib',
    author="Christian Zagrodnick",
    author_email="cz@gocept.com",
    description="FCKEditor integration into Zope 3",
    long_description="XXX",
    license="ZPL 2.1",
    url='https://bitbucket.org/gocept/gocept.fckeditor',

    include_package_data=True,
    zip_safe=False,

    install_requires=[
    ],
    extras_require={
        'test': [
            'zc.resourcelibrary',
            'zope.testbrowser',
            'zope.app.wsgi',
            'zope.app.zcmlfiles',
        ],
        'fanstatic': ['fanstatic'],
    },
    entry_points={
        'fanstatic.libraries': [
            'gocept_fckeditor=gocept.fckeditor.resources:lib',
        ],
    },
)
