from setuptools import setup

setup(
    name='alttp_multiworld_server',
    version='0.1',
    description='ALttPEntranceRandomizer multiworld server interface',
    long_description='Server interface and application for the ALttPEntranceRandomizer multiworld server',
    author='Daniel Aitken',
    maintainer='Daniel Aitken',
    maintainer_email='kyariester@gmail.com',
    url='https://github.com/qadan/alttp_multiworld_server',
    scripts=['bin/alttp_multiworld_server.py'],
    install_requires=[
        'flask',
        ],
    dependency_links=[
        'git+https://github.com/Bonta0/ALttPEntranceRandomizer.git',
        ]
        )
