from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="checkout",
    version="0.0.1",
    author_email="author@example.com",
    description="checkout test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        #"License :: OSI Approved :: MIT License",
        #"Operating System :: OS Independent",
    ],
)
