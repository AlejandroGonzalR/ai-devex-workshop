from setuptools import setup, find_packages

setup(
    name='scaffold',
    python_requires='>3.9',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click>=8.1.8,<8.2.0',
        'jinja2>=3.1.6,<3.2.0'
    ],
    entry_points='''
        [console_scripts]
        scaffold=scaffold.main:cli
    ''',
)

