from setuptools import setup, find_packages

setup(
    name="devin_onboarding",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
    ],
    python_requires=">=3.12",
    author="Seitaro Shinagawa",
    author_email="hirameki88888@gmail.com",
    description="A Python library project template for onboarding purposes",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SeitaroShinagawa/devin-onboarding",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
