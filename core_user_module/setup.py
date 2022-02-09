import setuptools

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name="core_user_module",
    version="0.0.2",
    author="Tntra",
    author_email="tntra@tntra.io",
    description="ddd package for sunrise ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    project_urls={
        "Bug Tracker": "",
    },
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    install_requires=REQUIREMENTS,
    python_requires=">=3.8",
)
