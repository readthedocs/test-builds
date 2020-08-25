import setuptools


setuptools.setup(
    name='test-builds',
    version="0.1.0",
    author='Manuel Kaufmann',
    author_email='humitos@gmail.com',
    description='Test-builds for Read the Docs',
    url='https://github.com/readthedocs/test-builds',
    license='MIT',
    packages=setuptools.find_packages(),
    long_description='Long description of the package',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Software Development :: Documentation',
    ],
    keywords='test builds read-the-docs',
    extras_require={
        'docs': [
            'readthedocs-ext @ git+https://${GITHUB_TOKEN}@github.com/readthedocs/readthedocs-ext/#egg=readthedocs-ext',
        ]
    }
)
