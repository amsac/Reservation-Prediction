from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="mlops-1-reservation-prediction",
    version="0.0.1",
    description="MLOps 1 Reservation Prediction",
    author="Akhil Vinayak",
    author_email="akhilvinayak@gmail.com",
    packages=find_packages(),
    install_requires=requirements,
)