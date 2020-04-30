import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-update", # Replace with your own username
    version="0.0.1",
    author="_ToOOom",
    author_email="yellow-submarine.dev@gmail.com",
    description="A python module that allows you to check for updates from a Github repository and install them",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://yellow-submarine215.github.io/py-update/",
    packages=setuptools.find_packages(),
    install_requires=['requests>=2.23.0'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
