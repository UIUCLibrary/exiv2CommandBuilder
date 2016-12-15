from setuptools import setup

setup(
    name='exiv2Driver',
    version='0.0.1a0',
    packages=['exiv2Driver'],
    scripts=['scripts/dummy.py'],
    test_suite="tests",
    tests_require=['pytest'],
    data_files=[
        ('settings', ['settings/exvsettings.ini']),
                ],
    zip_safe=False,
    url='',
    license='',
    author='Henry Borchers',
    author_email='hborcher@illinois.edu',
    description='Wrapper around exiv2'
)
