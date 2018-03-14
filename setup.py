import os
from setuptools import find_packages, setup


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-media-tools',
    version=__import__('media_tools').VERSION,
    packages=['media_tools'],
    include_package_data=True,
    license='MIT License',
    description='A Django app that provides widgets for media files',
    long_description=README,
    url='https://github.com/zeyneloz/django-media-tools',
    author='Zeynel',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)