from setuptools import setup

APP = ['weather.py']
OPTIONS = {'argv_emulation': True, 'includes': ['easygui'],}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)