from setuptools import setup


setup(
    name="pyconwaysgame",
    version="3.1.1",
    description="game of life",
    long_description="The complete description/installation/use/FAQ is available at : https://github.com/thib1984/pyconwaysgame#readme",
    url="https://github.com/thib1984/pyconwaysgame",
    author="thib1984",
    author_email="thibault.garcon@gmail.com",
    license="MIT",
    license_files="LICENSE.txt",
    packages=["pyconwaysgame"],
    install_requires=["columnar","click","termcolor","colorama"],
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "pyconwaysgame=pyconwaysgame.pyconwaysgame:pyconwaysgame"
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
