from setuptools import setup, find_packages

setup(
    name='squeezepics',
    version='1.0.0',
    description='A Python API for compressing images',
    long_description=readme,
    author='Nick Goehlert',
    author_email='nick.goehlert@gmail.com',
    packages=find_packages(),
    install_requires=[
        'Pillow',
    ],
)
