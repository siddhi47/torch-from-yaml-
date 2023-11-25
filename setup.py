from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

setup(
    name='torchfromyaml',
    version='0.0.1',
    description='A module to load pytorch models using yaml file',
    author='siddhi47',
    author_email='siddhi.47.skb ( a t ) gmail.com',
    packages = find_packages(),
    install_requires=[
        'torch',
        'pyyaml'
    ]
)