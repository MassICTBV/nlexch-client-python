from setuptools import setup

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name = "nlexch_client",
    version = "0.1.0",
    description = "a client library for the nlexch",
    url = 'https://github.com/MassICT/nlexch-client-python',
    long_description = readme(),
    author = "amarian12",
    license = "LGPL",
    keywords = "bitcoin nlexch nlexch.com",
    test_suite = "tests",
    packages = [
        "nlexch_client"
    ],
    install_requires = [
        "requests"
    ],
    zip_safe = False
)
