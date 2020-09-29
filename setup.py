import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(

    name="neuralplot",

    version="0.0.8",
 
    author="Rajkumar Soni",
 
    author_email="rajksoni029@gmail.com",
 
    description="A Library for visualizing Neural Networks.",
 
    long_description=long_description,
 
    long_description_content_type="text/markdown",

    url="https://github.com/Rajsoni03/neuralplot",

    py_modules=["neuralplot"],

    package_dir={"": "src"},

    install_requires=[
        "matplotlib>=3.1"
        "numpy>=1.16"
    ],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)