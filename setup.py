from setuptools import setup, find_packages
from distutils.version import LooseVersion
import sys

if LooseVersion(sys.version) < LooseVersion("3.4.0"):
    print("piratebay-scraper requires at least python 3.4.0."
          " Your version is %s." % sys.version.split()[0])
    sys.exit(1)

if __name__ == '__main__':
    setup(name='piratebay-scraper',
        version=1.0,
        description='A command line interface for The Pirate Bay',
        url='https://github.com/MasterChief-kun',
        author='MasterChief-kun',
        license='GPL-3',
        packages=find_packages(),
        entry_points={
            'console_scripts': ['pirate-get = pirate.pirate:main']
        },
        install_requires=['bs4==0.0.1',
                          'prettytable==2.0.0',
                          'selenium==3.141.0'],
        keywords=['torrent', 'magnet', 'download', 'tpb', 'client'],
        classifiers=[
            'Topic :: Utilities',
            'Topic :: Terminals',
            'Topic :: System :: Networking',
            'Programming Language :: Python :: 3 :: Only',
            'Programming Language :: Python :: 3.4',
            'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
        )
