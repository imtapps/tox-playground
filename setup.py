from distutils.core import setup


setup(
        name='mytest',
        version='0.0.1',
        install_requires=file('requirements/base.txt').read().split('\n'),
        include_package_data=True,
        packages=['mycode'],
)
