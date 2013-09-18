#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='django-inline-orderable',
    version='0.1.1',
    author='Marco Fucci',
    author_email='info@marcofucci.com',
    url='https://github.com/marcofucci/django-inline-orderable',
    description='An easy way of making inlines orderable using drag-and-drop.',
    license='BSD',
    packages=find_packages(),
    provides=['inline_orderable',],
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
