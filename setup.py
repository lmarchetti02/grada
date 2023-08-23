from setuptools import find_packages, setup

setup(
    name="grada",
    packages=find_packages(include=["grada"]),
    version="0.1.0",
    description="A short project for rapidly graphing beautiful datasets and fit curves.",
    author="Luca Marchetti",
    license="MIT",
    install_requires=["matplotlib", "logging"],
)
