import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="active911_python",
    version="0.0.4",
    author="David Chason",
    author_email="davidchason@gmail.com",
    description="Python bindings for active911 API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dc105297/active911_python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
