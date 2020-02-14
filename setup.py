from codecs import open
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') \
        as f: long_description = f.read()

setup(name='2d_souls',
      version='1.0.1',
      description='Das Dark Souls unter den Informatikprojekten',
      long_description=long_description,
      long_description_content_type='text/markdown',
      keywords=['games', 'education', 'mini-worlds', 'miniworldmaker'],  # arbitrary keywords
      author='',
      author_email='',
      url='',
      download_url='',
      license="GNU GENERAL PUBLIC LICENSE",
      classifiers=["License :: GNU GENERAL PUBLIC LICENSE",
                   "Programming Language :: Python",
                   "Development Status :: 4 - Beta",
                   "Intended Audience :: Games",
                   "Topic :: Games",
                   ],
      package_dir={'project': 'project'},
      install_requires=['miniworldmaker', 'mathplotlib', 'pygame'],
      include_package_data=True,
      )
