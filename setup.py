from setuptools import setup

setup(
    name='pysoserial',
    version='1.0.1',
    packages=[''],
    url='https://github.com/itasahobby/pysoserial.git',
    license='',
    author='ITasahobby',
    author_email='ITasahobby@gmail.com',
    description='Python deserialization payload generator',
    install_requires=[
        'jsonpickle==2.0.0',
        'pylint==2.11.1',
        'PyYAML==6.0'
    ],
    entry_points={
        'console_scripts': [
            'pysoserial = pysoserial:main',
        ],
    },
)
