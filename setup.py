from setuptools import setup, find_packages
from os.path import join, dirname
import timetable2json


setup(
    entry_points={
        'console_scripts': [
            'timetable2json = timetable2json.timetable2json:main'
        ]
    },
    name='timetable2json',
    version=timetable2json.__version__,
    packages=find_packages(),
    install_requires=[
        'xlrd',
        'pandas'
    ],
    long_description=open(join(dirname(__file__), 'README.md')).read(),
)