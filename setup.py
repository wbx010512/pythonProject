import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example_packg",
    version="0.0.1",
    author="wbx",
    author_email="wbx481742959@Outlook.com",
    description="a example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wbx010512/pythonProject.git",
    packages=setuptools.find_packages(),
    install_requires=[''],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)