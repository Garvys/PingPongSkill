from setuptools import setup

setup(
    name='ping_pong_skill',
    version='0.0.1',
    description='My skill for Snips',
    url='https://github.com/Garvys/PingPongSkill',
    download_url='',
    license='MIT',
    install_requires=['requests==2.6.0'],
    test_suite="tests",
    keywords=['snips'],
    packages=['ping_pong_skill'],
    package_data={'myskill': ['Snipsspec']},
    install_requires=[
        'peewee',
    ],
    include_package_data=True,
)
