from setuptools import setup, find_packages

setup(
    name='dupecleaner',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dupecleaner = main:main',  # assumes main.py has a main() function
        ],
    },
)