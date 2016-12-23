from setuptools import setup

setup(
    name='mywebsite',
    packages=['mywebsite'],
    include_package_data=True,
    install_requires=[
        'flask',
        'redis'
    ],
)