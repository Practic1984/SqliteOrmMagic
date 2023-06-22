from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="SqliteOrmMagic",
    version="0.0.1",
    author="Practic_old",
    author_email="tda.kub@gmail.com",
    description="Facilitates the complex syntax of SQL queries through the use of standard commands for reading / writing to the SQlite3 database in Python program",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/your_package/homepage/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
    ],
)