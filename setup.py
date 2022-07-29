import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = [
    "xlwings>=0.27.11",
    "pretty-repr>=1.0.4",
    "math_round_af>=1.0.3",
]

setuptools.setup(
    name="excel_af",
    version="0.0.5",
    author="Albert Farkhutdinov",
    author_email="albertfarhutdinov@gmail.com",
    description="Python package to work with Microsoft Excel files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlbertFarhutdinov/excel_af",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
    python_requires='>=3.6',
)
