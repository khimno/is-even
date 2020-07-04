import setuptools

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="is-even",
    version="0.0.1",
    author="khimno",
    author_email="khimnodev@gmail.com",
    description="Library to check if a given integer or string is an even number",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/khimno/is-even",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7.5',
)
