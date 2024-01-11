from setuptools import setup, find_packages

setup(
    name='mytorchvis',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'torchview',  # Include any dependencies here
        'graphviz',
    ],
)
