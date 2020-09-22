from setuptools import setup, find_packages
from re import search, M as MULTILINE


def _open(file):
    with open(file) as f:
        return f.read()


version = search(
    r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
    _open('zuraaaVoteChecker/__init__.py'), MULTILINE
).group(1)


setup(
    name='zuraaa-vote-checker',
    version=version,
    description='Um coletor de votos no Zuraaa.',
    long_description=_open('README.rst'),

    author='uKaigo',
    license='MIT',

    url='https://github.com/uKaigo/zuraaa-vote-checker',
    project_urls={
        'Issues': 'https://github.com/uKaigo/zuraaa-vote-checker/issues'
    },

    packages=find_packages(),

    install_requires=_open('requirements.txt'),
    python_requires='>=3.6',

    include_package_data=True,

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: Portuguese',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet',
        'Topic :: Utilities',
      ]
)
