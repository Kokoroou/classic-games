import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ttanh_games",
    version="0.1.0",
    author="Kokoroou",
    author_email="truongtuananh.projects@gmail.com",
    description="A package of classic games",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kokoroou/classic_games",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=[
        "pygame",
    ],
)
