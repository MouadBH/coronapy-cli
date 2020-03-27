from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="coronapy-cli",
    version="0.0.1",
    author="MouadBH",
    author_email="mouad123b@gmail.com",
    description="A command line tool to fetch worldwide data about Corona Virus",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MouadBH/coronapy-cli",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)