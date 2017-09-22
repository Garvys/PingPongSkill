from setuptools import setup

setup(
    name='myskill',
    version='0.0.1',
    description='My skill for Snips',
    url='https://github.com/snipsco/snips-skill-skeleton',
    download_url='',
    license='MIT',
    install_requires=['requests==2.6.0'],
    test_suite="tests",
    keywords=['snips'],
    packages=['myskill'],
    package_data={'myskill': ['Snipsspec']},
    include_package_data=True,
)
