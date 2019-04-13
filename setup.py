__version__ = '0.1.0'

from setuptools import setup

setup(
    name='storedoc',
    version=__version__,
    description='A python module to upload files on cloud. Supported services - AWS S3, DigitalOcean Spaces, LocalStorage.',
    long_description='',
    author='Rakesh Gunduka',
    author_email='rakesh.gunduka@gmail.com',
    install_requires=['boto3'],
    license='http://www.opensource.org/licenses/mit-license.php',
    keywords='',
    scripts=[
        'storedoc/local.py', 'storedoc/services.py',
        'storedoc/s3.py', 'storedoc/spaces.py'
    ],
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent'
    ]
)
