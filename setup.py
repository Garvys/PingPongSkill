from setuptools import setup

setup(
    name='pingpongskill',
    version='0.0.1',
    description='My skill for Snips',
    url='https://github.com/Garvys/PingPongSkill',
    download_url='',
    license='MIT',
    install_requires=['requests==2.6.0', 'peewee'],
    test_suite="tests",
    keywords=['snips'],
    packages=['pingpongskill'],
    package_data={'myskill': ['Snipsspec']},
    include_package_data=True,
)
