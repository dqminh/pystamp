"""
Pystamp
-----------

datetime formatting for human. This is a fork on
`https://github.com/jeremyw/stamp`_ , written in Python

Links
`````

* `documentation <https://github.com/dqminh`_
* `development version
  <https://github.com/dqminh/pystamp#egg=pystamp-dev>`_
"""
from setuptools import setup


setup(
    name='Pystamp',
    version='0.0.1',
    url='https://github.com/dqminh/pystamp/',
    license='BSD',
    author='Daniel, Dao Quang Minh',
    author_email='dqminh89@gmail.com',
    description='datetime formatting for human',
    long_description=__doc__,
    packages=['pystamp'],
    namespace_packages=['pystamp'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[],
    test_suite='pystamp.test',
    tests_require=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
