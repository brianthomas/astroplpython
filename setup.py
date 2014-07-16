
from setuptools import setup, find_packages, Command 
from setuptools.command.test import test as TestCommand

class PyTest(Command):

    user_options = []
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys,subprocess
        errno = subprocess.call ([sys.executable, 'run_tests.py'])
        raise SystemExit(errno)


setup (

    name='AstroPLPython',
    description='PL/Python package for astronomy',
    url='https://www.github.com/brianthomas/astroplpython',
    version='0.1',

    keywords = 'plpython astronomy',
#    long_description=open('README.md').read(),

    maintainer='Brian Thomas',
    maintainer_email='galactictaco@gmail.com',

#    packages=['astroplpython/*', 'tests', 'sql'],
    packages=find_packages(),
    license='MIT License',

    package_data = {
        # If any package contains *.txt or *.md files, include them:
        '': ['*.txt', 'README.md'],
        # And include any *.sql files found in the sql package, too:
        'astroplpython': ['*.sql'],
    },

    cmdclass = {'test': PyTest},
    #test_loader = 'unittest:TestLoader', 
    #test_suite = 'astroplpython.proc.test.test_LSPeriodogram',
    #test_suite = 'astroplpython.proc.test.test_LSPeriodogram',

)

