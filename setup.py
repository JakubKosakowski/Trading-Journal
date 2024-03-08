from setuptools import setup

setup(
    name='trading-journal',
    version='1',
    entry_points={
        'console_scripts': ['trading-journal=scripts.app:main'],
    }
)