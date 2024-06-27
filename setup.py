from setuptools import find_packages, setup

with open("README.md", 'r') as readme:
    package_description = readme.read()

setup(
    name="rotating-logger",
    version="0.1.0",
    packages=find_packages(),
    author="Romain MRAD",
    author_email="romain.mrad@gmail.com",
    url="https://github.com/romainmrad/rotating_logger.git",
    description="Python Rotating Logger",
    long_description=package_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
