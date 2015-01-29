
from os.path import dirname, join
from setuptools import setup, find_packages, Command 

try:
    from setupext import janitor
    CleanCommand = janitor.CleanCommand
except ImportError:
    CleanCommand = None

cmd_classes = {}
if CleanCommand is not None:
    cmd_classes['clean'] = CleanCommand

with open(join(dirname(__file__), 'astroplpython/VERSION'), 'rb') as f:
	version = f.read().decode('ascii').strip()

with open(join(dirname(__file__), 'README.md'), 'rb') as f:
	long_description = f.read().decode('ascii').strip()

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

    include_package_data=True,

#    setup_requires=['setupext.janitor'],
    cmdclass = cmd_classes,

    install_requires=[
        'scipy==0.15.1',
    ],

)

