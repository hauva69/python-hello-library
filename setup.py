from setuptools import find_packages, setup

setup(
    name='hello',
    packages=find_packages(include=['hello']),
    version='0.0.1',
    description='A hello library',
    author='ari.makela@iki.fi',
    license='MIT',
    install_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
