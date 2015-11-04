from setuptools import setup

setup(
    # GETTING-STARTED: set your app name:
    name='{{cookiecutter.repo_name}}',
    # GETTING-STARTED: set your app version:
    version='{{cookiecutter.version}}',
    # GETTING-STARTED: set your app description:
    description='{{cookiecutter.description}}',
    # GETTING-STARTED: set author name (your name):
    author='{{cookiecutter.author_name}}',
    # GETTING-STARTED: set author email (your email):
    author_email='{{cookiecutter.email}}',
    # GETTING-STARTED: set author url (your url):
    url='{{cookiecutter.domain_name}}',
    # GETTING-STARTED: define required django version:
    install_requires=[
        'Django==1.8.4',
        'waitress', 'dj-paas-env>=0.6.1', 'dj-static', 'psycopg2'
    ],
    dependency_links=[
        'https://pypi.python.org/simple/django/'
    ],
)