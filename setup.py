import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pkgzzztest",                            # This is the name of the package
    version="0.0.2",                              # The initial release version
    author="Example Author",                      # Full name of the author
    author_email="author@example.com",            # email
    description="A small example package",        # description
    long_description=long_description,            # Long description read from the the readme file
    long_description_content_type="text/markdown",# 
    url="https://github.com/PepperPapa/xinNotes",
    packages=setuptools.find_packages(),          # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                            # Information to filter the project on PyPi website
    python_requires='>=3.6',                      # Minimum version requirement of the package
    py_modules=["pkgzzztest"],                    # Name of the python package
    package_dir={'':'pkgzzztest'},                # Directory of the source code of the package
    install_requires=[]                           # Install other dependencies if any
)
