

from os.path import dirname, join

from setuptools import setup, find_packages, Command 
from setuptools.command.test import test as TestCommand

with open(join(dirname(__file__), 'astroplpython/VERSION'), 'rb') as f:
	version = f.read().decode('ascii').strip()

with open(join(dirname(__file__), 'README.md'), 'rb') as f:
	long_description = f.read().decode('ascii').strip()

import os
class PyTest(Command):

    description = "custom test command that uses special run_test.py script built by py.test --genscript"

    user_options = []
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys,subprocess
        errno = subprocess.call ([sys.executable, 'bin/run_tests.py'])
        raise SystemExit(errno)

class CleanCommand(Command):

    description = "custom clean command that forcefully removes dist/build directories"

    user_options = []
    def initialize_options(self):
        self.cwd = None

    def finalize_options(self):
        self.cwd = os.getcwd()

    def run(self):
        assert os.getcwd() == self.cwd, 'Must be in package root: %s' % self.cwd
        os.system('rm -rf ./build ./dist *.egg-info')

setup (

    name='AstroPLPython',
    description='PL/Python package for astronomy',
    url='https://www.github.com/brianthomas/astroplpython',
    version=version,

    keywords = 'plpython astronomy',
    long_description=long_description,

    maintainer='Brian Thomas',
    maintainer_email='galactictaco@gmail.com',

    packages=find_packages(exclude=('tests', 'tests.*')),
    license='MIT License',

    package_data = {
        # If any package contains *.txt or *.md files, include them:
        '': ['*.txt', 'README.md'],
        # And include any *.sql files found in the sql package, too:
        'astroplpython': ['*.sql'],
    },

    cmdclass = {
	'distclean': CleanCommand,
	'test': PyTest
    },

)

