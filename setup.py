
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages 

setup (

    name='AstroPLPython',
    description='PL/Python package for astronomy',
    url='https://www.github.com/brianthomas/astroplpython',
    version='0.1',

    keywords = 'plpython astronomy',
    long_description=open('README.md').read(),

    maintainer='Brian Thomas',
    maintainer_email='galactictaco@gmail.com',

#    packages=['astroplpython/*', 'tests', 'sql'],
    packages=find_packages(),
    license='MIT License',

    package_data = {
        # If any package contains *.txt or *.md files, include them:
        '': ['*.txt', '*.md'],
        # And include any *.sql files found in the sql package, too:
        'astroplpython': ['*.sql'],
    },

    test_suite = "astroplpython", 
)

