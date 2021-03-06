from setuptools import setup

with open('requirements.txt') as read_file:
    REQUIRED = read_file.read().splitlines()

setup(
    name='sc3nb',
    version='0.0.1',
    description='SuperCollider3 (sc3) jupyter notebook class and magics',
    license='MIT',
    packages=['sc3nb'],
    install_requires=REQUIRED,
    author='Thomas Hermann',
    author_email='thermann@techfak.uni-bielefeld.de',
    keywords=['sonification, sound synthesis'],
    url='https://github.com/thomas-hermann/sc3nb'
)
