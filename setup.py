from setuptools import find_packages, setup

setup(
    name="graphs_for_science",
    packages=find_packages(include=["graphs_for_science"]),
    version="0.1.0",
    description="A short project for rapidly graphing beautiful datasets and fit curves.",
    author="Luca Marchetti",
    license="MIT",
    install_requires=["matplotlib", "logging"],
)
