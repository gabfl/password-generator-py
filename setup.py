from setuptools import setup

setup (
    name = 'passwordgenerator',
    version = '1.0.2',
    description = 'Python password manager',
    author = 'Gabriel Bordeaux',
    author_email = 'pypi@gab.lc',
    url = 'https://github.com/gabfl/password-generator-py/',
    license = 'MIT',
    packages = ['passwordgenerator'],
    package_data={
        'passwordgenerator': ['data/*.csv'],
    },
    entry_points = {
        'console_scripts': [
            'passwordgenerator = passwordgenerator.passwordgenerator:main',
        ],
    },
)
