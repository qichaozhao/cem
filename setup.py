#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'pandas>=1.0',
    'scipy>=1.4',
    'numpy>=1.18',
    'tqdm>=4.46',
]

setup_requirements = []

test_requirements = []

setup(
    author="Lewis Bails",
    author_email='lewis.bails@gmail.com',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A Python implmentation of Coarsened Exact Matching for causal inference",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='cem',
    name='cem',
    packages=find_packages(include=['cem', 'cem.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/lewisbails/cem',
    version='0.1.3',
    zip_safe=False,
)
