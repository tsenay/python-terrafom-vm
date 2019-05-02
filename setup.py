import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='terraform-vm',
    version='0.3',
    scripts=['terraform-vm'],
    author="Thomas Senay",
    author_email="tsenay.consulting@icloud.com",
    description="A tool to Manage VM into vSphere",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tsenay/python-terraform-vm",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'terrascript', 'python_terraform'
    ],
)
