from setuptools import setup


setup(
    name="pyconwaysgame",
    version="2.1.1",
    description="game of life",
    long_description="The complete description/installation/use/FAQ is available at : https://github.com/thib1984/pyconwaysgame#readme",
    url="https://github.com/thib1984/pyconwaysgame",
    author="thib1984",
    author_email="thibault.garcon@gmail.com",
    license="MIT",
    packages=["pyconwaysgame"],
    install_requires=["columnar","click","termcolor","colorama"],
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "pyconwaysgame=pyconwaysgame.pyconwaysgame:pyconwaysgame"
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",        
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)
