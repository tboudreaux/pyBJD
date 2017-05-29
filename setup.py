from setuptools import setup
from os import path

__version__ = 1.0

setup(name='pyBJD',
	  version=1.0,
	  description='A Very Basic JD to BJD conversion API',
	  url='https://github.com/tboudreaux/pyBJD',
	  author='Thomas Boudreaux',
	  author_email='thomas@boudreauxmail.com',
	  license='MIT',
	  classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3'
      ],
      install_requires=['astropy>=1.3.2',
      					'numpy>=1.12.0',
      					'selenium>=3.4.2'],
      packages=['pyBJD'],
      zip_safe=False
	)
