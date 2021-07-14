import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = ["xlwings>=0.24.2"]

setuptools.setup(
    name="excel_af",
    version="0.0.1",
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
    # Требуемая версия Python.
    python_requires='>=3.6',
)
