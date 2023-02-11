from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name='squeezepics',
    version='1.0.0',
    description='A Python API for compressing images',
    long_description=readme,
    author='Nick Goehlert',
    author_email='nick.goehlert@gmail.com',
    url='https://github.com/nigo2000/squeezepics',
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
