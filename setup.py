from setuptools import setup

setup(
    name='exiv2CommandBuilder',
    version='0.0.1b0',
    packages=['exiv2Driver'],
    scripts=['scripts/dummy.py'],
    test_suite="tests",
    tests_require=['pytest'],
    data_files=[
        ('settings', ['settings/settings.ini']),
                ],
    zip_safe=False,
    url='',
    license='',
    author='Henry Borchers',
    author_email='hborcher@illinois.edu',
    description='Command builder for exiv2'
)
