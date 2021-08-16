"""
    ShareImage - A Python Library to Generate Dynamic Share Images.
"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ShareImage",
    version="2.1.0",
    maintainer="Rajdeep Malakar",
    maintainer_email="Rajdeep@zype.cf",
    author="Zype Inc.",
    author_email="info@zype.cf",
    description="A Python Library to Generate Dynamic Share Images. Powered by Cloudinary.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Zype-Z/ShareImage",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
