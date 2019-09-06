#! /usr/bin/env python
from setuptools import setup

if __name__ == "__main__":
    setup(
        name='iem-concerns',
        version='0.1',
        description='Development of IEM concerns',
        long_description=open('README.md').read(),
        url='',
        author='Takuya Iwanaga',
        author_email='iwanaga.takuya@anu.edu.au',
        license='(c) 2018 Takuya Iwanaga',
        dependency_links=[
            'pip install git+https://github.com/ConnectedSystems/metaknowledge.git@add-collections',
            'pip install git+https://github.com/titipata/wos_parser.git@master',
            'pip install git+https://github.com/ConnectedSystems/restful_wos.git@master',
            'pip install git+https://github.com/ConnectedSystems/wosis.git@master',
        ],
    )
