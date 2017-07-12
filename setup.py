from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='passwordgenerator',
    version='1.1',
    description='Passwords easy for humans, hard for computers',
    long_description=long_description,
    author='Gabriel Bordeaux',
    author_email='pypi@gab.lc',
    url='https://github.com/gabfl/password-generator-py/',
    license='MIT',
    packages=['passwordgenerator', 'passwordgenerator.data'],
    package_dir={'passwordgenerator': 'src'},
    install_requires=['argparse'],  # external dependencies
    entry_points={
        'console_scripts': [
            'passwordgenerator = passwordgenerator.pwgenerator:main',
        ],
    },
)
