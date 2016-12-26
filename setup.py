from setuptools import setup

setup(
    name='mywebsite',
    packages=['mywebsite'],
    include_package_data=True,
    install_requires=[
        'click',
        'Flask',
        'Flask-FlatPages',
        'itsdangerous',
        'Jinja2',
        'Markdown',
        'MarkupSafe',
        'Pygments',
        'PyYAML',
        'redis',
        'Werkzeug'
    ],
)