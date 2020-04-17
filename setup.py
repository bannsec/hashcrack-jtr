# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
import os, sys, ast

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "hashcrack_jtr", "version.py"), "r") as f:
    exec(f.read())

with open(os.path.join(here, 'pypi.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='hashcrack-jtr',
    version=version,
    description='CLI install of John-the-Ripper for hashcrack.',
    long_description=long_description,
    url='https://github.com/bannsec/hashcrack-jtr',
    author='Michael Bann',
    author_email='self@bannsecurity.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Environment :: Console'
    ],
    keywords='password cracking john jtr',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['prettytable', 'appdirs', 'prompt-toolkit'],
    extras_require={
        'dev': ['ipython','twine','pytest','python-coveralls','coverage==4.5.4','pytest-cov','pytest-xdist','sphinxcontrib-napoleon', 'sphinx_rtd_theme','sphinx-autodoc-typehints', 'restview'],
    },
    entry_points={
        'console_scripts': [
            'john = hashcrack_jtr.john:cli_john',
            'zip2john = hashcrack_jtr.john:cli_zip2john',
            'rar2john = hashcrack_jtr.john:cli_rar2john',
            'gpg2john = hashcrack_jtr.john:cli_gpg2john',
            'unafs = hashcrack_jtr.john:cli_unafs',
            'undrop = hashcrack_jtr.john:cli_undrop',
            'unshadow = hashcrack_jtr.john:cli_unshadow',
        ],
    },
    include_package_data = True,
)

