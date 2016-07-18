from setuptools import setup, find_packages


with open('README.md') as f:
    readme_text = f.read()

with open('LICENSE') as f:
    license_text = f.read()

setup(
    name='example',
    version='0.0.1',
    description='Example Python package for park.mail.ru',
    long_description=readme_text,
    author='Alexandr Emelin',
    author_email='emelin@corp.mail.ru',
    url='https://github.com/park-python/python-project-template',
    license=license_text,
    packages=find_packages(exclude=('tests',))
)
