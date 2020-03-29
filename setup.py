from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setup(
    name="coronapy-cli",
    version="1.2.3",
    author="MouadBH",
    author_email="mouad123b@gmail.com",
    description="A command line tool to fetch worldwide data about Corona Virus",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords = ['corona', 'covid-19', 'cli', 'corona-cli'], 
    url="https://github.com/MouadBH/coronapy-cli",
    license="MIT",
    packages=find_packages(),
    package_data={},
    install_requires=['Click', 'pyfiglet', 'prettytable', 'yaspin', 'termgraph', 'colorama', 'termcolor'],
    entry_points='''
        [console_scripts]
        coronapy=coronapy.cli:cli
    ''',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)