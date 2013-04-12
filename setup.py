"""
setup.py
"""

from distutils.core import setup

setup(name='alpaca',
      version='1.0.0',
      scripts=['src/alpaca.py'],
      package_dir={'': 'src'},
      packages=['alpacalib'],
      author='Bo Wangbo',
      author_email='activesys.wb@gmail.com',
      url='https://github.com/activesys/alpaca-llama',
      license='BSD')

